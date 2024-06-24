from __future__ import annotations
import typing
from llm import ChatBotLLM
import json
import typing
from utils import ensemble, process_output, convert_score, process_token
from tqdm import tqdm
from evaluation import BaseEvaluation, Config
from prompt_evaluation import PromptEngineerEvaluation
import numpy as np
from transformers import StoppingCriteria
import torch
from queue import PriorityQueue


class Node:
    def __init__(self, code: str, history: str, value: int, depth: int) -> None:
        self.code = code
        self.history = history
        self.value = value
        self.depth = depth
    
    def get_value(self) -> float:
        return self.value
    
    def __lt__(self, other) -> bool:
        return self.get_value() > other.get_value()
    

class LineStoppingCriteria(StoppingCriteria):
    def __init__(self, eos_sequence):
        self.eos_sequence = eos_sequence

    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor, **kwargs) -> bool:
        last_ids = list(map(lambda x: x[0], input_ids[:,-len(self.eos_sequence):].tolist()))
        return self.eos_sequence[0] in last_ids


class PromptToT(PromptEngineerEvaluation):

    def __init__(self, model: ChatBotLLM, data_path: str, config: Config, prompt_template: str, top_b1=3, top_b2=5, max_depth=50, **kwargs) -> None:
        super().__init__(model, data_path, config, prompt_template, **kwargs)
        self.top_b1 = top_b1
        self.top_b2 = top_b2
        self.stopping_criteria = ["\n"]
        self.max_depth = max_depth


    def getModelOutput(self, prompt: str, num_responses=1) -> list[Node]:
        self.model.clear_chat_history()
        self.model.update_system_prompt("You are an Operational Research professor who can solve optimization problems with python code.")
        few_shots = prompt.split("#### Problem ####")
        for shot in few_shots[:-1]:
            if len(shot) == 0: 
                continue
            qa = shot.split("#### Solution ####")
            question, answer = qa[0], qa[1]
            self.model.add_user_message(f"""Give a step by step reasoning and python code to solve the following Optimization problem. Wrap the print statements between "## start solving" and "## end solving". Only print what the reqirements requires.
{question}""")
            self.model.add_assistant_message(answer)

        prompt = few_shots[-1].split("#### Solution ####")[0]

        self.model._messages.append_user_message(f"""Give a step by step reasoning and python code to solve the following Optimization problem. Wrap the print statements between "## start solving" and "## end solving". Only print what the reqirements requires.
{prompt}""")

        chat_history = self.model._tokenizer.apply_chat_template(
            self.model._messages.get_all_messages(), 
            tokenize=False, 
            add_generation_prompt=True,
        )

        code = ""
        frontier = PriorityQueue()

        frontier.put(Node(
            code=code,
            history=chat_history,
            value=0,
            depth=1,
        ))
        
        terminal_states: list[Node] = []
        
        depth = 1
        while len(terminal_states) < self.top_b1 * self.top_b2 and depth <= self.max_depth:
            elem_cnt = 0
            cur_frontier = []
            # Get the top-b1
            while not frontier.empty() and elem_cnt < self.top_b1:
                cur_frontier.append(frontier.get())
                elem_cnt += 1
            
            # Sample top_b2
            generated_codes = self.next_state([cur_node.history for cur_node in cur_frontier], beam_width=self.top_b2)
            new_codes: list[tuple[Node, str]] = []
            for cur_node, generated_code in zip(cur_frontier, generated_codes):
                for code in generated_code:
                    if code == "from pulp":
                        code = "from pulp import *"
                    new_codes.append((cur_node, code))
            values = self.heuristic(prompt, [cur_node.code + code for cur_node, code in new_codes])

            for (cur_node, new_code), value in zip(new_codes, values):
                # Terminal state
                if new_code.find(r'print("## end solving")') != -1:
                    terminal_states.append(cur_node.code + '\nprint("## end solving")')
                    continue
                new_node = Node(
                    code = cur_node.code + new_code + '\n',
                    history = cur_node.history + new_code + '\n',
                    value = cur_node.value + value,
                    depth = cur_node.depth + 1,
                )
                frontier.put(new_node)
                
            depth += 1
            
        return terminal_states
    
    def getParsedModelOutput(self, prompt: str, id: int, num_answers: int, num_responses=1) -> list[float]:
        list_model_outputs = self.getModelOutput(prompt, num_responses)
        list_parsed_output: list[tuple[float]] = []
        for model_output in list_model_outputs:
            parsed_output = process_output(model_output, id)
            if parsed_output is None or len(parsed_output) == 0:
                continue
            
            if len(parsed_output) < num_answers:
                excess = num_answers - len(parsed_output)
                parsed_output.extend([0 for i in range(excess)])
            elif len(parsed_output) > num_answers:
                parsed_output = parsed_output[:num_answers]
                
                
            list_parsed_output.append(tuple(parsed_output))
        
        if len(list_parsed_output) == 0:
            parsed_output = [0 for i in range(num_answers)]
        else:
            parsed_output = ensemble(list_parsed_output)
            
        return self.convertToFloatList(parsed_output)
    

    def submit(self) -> list[dict[str, str]]:
        submission: list[dict[str, str]] = []
        for task in tqdm(self.data):
            id = task["id"]
            answers = list(task["results"].keys())
            question = task["question"]

            formatted_answers = '\n'.join(list(map(lambda s: s + ": ?", answers)))

            prompt = self.prompt_template.format(question, formatted_answers)

            parsed_output = self.getParsedModelOutput(prompt, id, len(answers))

            task_submission = {}
            for key, val in zip(answers, parsed_output):
                task_submission[key] = str(val)

            submission.append(task_submission)

        return submission
    

    def next_state(self, prev_state, beam_width=5):
        model_output = self.model.get_response(
            prompts=prev_state,
            max_new_tokens=2048,
            temperature=0.8,
            top_p=0.9,
            stop_criteria=self.stopping_criteria,
            num_return_sequences=beam_width,
        )
        return model_output
    
    
    def heuristic(self, problem: str, codes: str) -> int:
        scores = self.model.get_response(
            prompts=[self.get_eval_prompt(problem, code) for code in codes],
            max_new_tokens=1,
            top_p=0.5,
            temperature=0.001,
            num_return_sequences=1,
            processor=process_token,
        )
        return [convert_score(score[0]) for score in scores]
        
        
    def get_eval_prompt(self, problem: str, code: str) -> list[str]:
        message = [
            {
                "role": "system",
                "content": "You are an Operational Research Professor who needs to grade students' solution.",
            },
            {
                "role": "user",
                "content": f"""You will be given a Linear Programming problem and the current solution steps that might not completed yet. Give the solution a score from 0 (bad) to 9 (good) that represents how good the reasoning is to solve the problem.

The student's solution will contains two part: reasoning and python code.

In both reasoning and python code, there are 4 main sections:
- Define the decision variables
- Define the question as a maximum or minimum problem
- Define the objective function
- Define the constraints

####Problem####
{problem}
####Current Solution####
{code}"""
            },
            {
                "role": "assistant",
                "content": "The student's score is: ",
            },
        ]

        return self.model._tokenizer.apply_chat_template(
            message,
            tokenize=False, 
            add_generation_prompt=False,
        )