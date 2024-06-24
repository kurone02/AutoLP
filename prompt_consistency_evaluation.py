from llm import ChatBotLLM
import json
import typing
from utils import ensemble 
from tqdm import tqdm
from evaluation import BaseEvaluation, Config
from prompt_evaluation import PromptEngineerEvaluation
import numpy as np

class PromptConsistencyEngineerEvaluation(PromptEngineerEvaluation):

    def __init__(self, model: ChatBotLLM, data_path: str, config: Config, prompt_template: str, num_trials: int=5, **kwargs) -> None:
        super().__init__(model, data_path, config, prompt_template, **kwargs)
        self.num_trials = num_trials

    def submit(self) -> list[dict[str, str]]:
        submission: list[dict[str, str]] = []
        for task in tqdm(self.data):
            id = task["id"]
            answers = list(task["results"].keys())
            question = task["question"]

            formatted_answers = '\n'.join(list(map(lambda s: s + ": ?", answers)))

            list_parsed_output: list[tuple[float]] = []

            prompt = self.prompt_template.format(question, formatted_answers)
            parsed_outputs = self.getParsedModelOutput(prompt, id, num_responses=self.num_trials)

            for i in range(self.num_trials):
                parsed_output = parsed_outputs[i]

                if parsed_output is None or len(parsed_output) == 0:
                    continue

                if len(parsed_output) < len(answers):
                    excess = len(answers) - len(parsed_output)
                    parsed_output.extend([0 for i in range(excess)])
                elif len(parsed_output) > len(answers):
                    parsed_output = parsed_output[:len(answers)]

                list_parsed_output.append(tuple(parsed_output))


            if len(list_parsed_output) == 0:
                parsed_output = [0 for i in range(len(answers))]
            else:
                parsed_output = ensemble(list_parsed_output)

            task_submission = {}
            for key, val in zip(answers, parsed_output):
                task_submission[key] = str(val)

            submission.append(task_submission)

        return submission