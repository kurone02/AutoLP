from llm import ChatBotLLM
import json
import typing
from utils import process_output
from tqdm import tqdm
from evaluation import BaseEvaluation, Config
import numpy as np

class PromptEngineerEvaluation(BaseEvaluation):

    prompt_template: str

    def __init__(self, model: ChatBotLLM, data_path: str, config: Config, prompt_template: str, **kwargs) -> None:
        super().__init__(model, data_path, config, **kwargs)
        self.prompt_template = prompt_template

    def eval(self) -> float:
        raise NotImplementedError()
    
    def submit(self) -> list[dict[str, str]]:
        submission: list[dict[str, str]] = []
        for task in tqdm(self.data):
            id = task["id"]
            answers = list(task["results"].keys())
            question = task["question"]

            formatted_answers = '\n'.join(list(map(lambda s: f"    * {s}: ?" , answers)))

            prompt = self.prompt_template.format(question, formatted_answers)
            parsed_output = self.getParsedModelOutput(prompt, id)

            if parsed_output is None:
                task_submission = {}
                for key in answers:
                    task_submission[key] = str(0.0)

                submission.append(task_submission)
                continue

            if len(parsed_output) < len(answers):
                excess = len(answers) - len(parsed_output)
                parsed_output.extend([0 for i in range(excess)])
            elif len(parsed_output) > len(answers):
                parsed_output = parsed_output[:len(answers)]

            task_submission = {}
            for key, val in zip(answers, parsed_output):
                task_submission[key] = str(val)

            submission.append(task_submission)
        
        return submission