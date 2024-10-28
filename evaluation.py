from .llm import BaseLLM, ChatBotLLM
import json
import typing
from .utils import process_output
from tqdm import tqdm
from math import isclose
from functools import reduce
import numpy as np
import numpy.typing as npt
from datasets import Dataset

class DataPoint(typing.TypedDict):
    id: int
    question: str
    code: str
    results: dict

class Config(typing.TypedDict):
    max_new_tokens: int
    temperature: float
    top_p: float


class BaseEvaluation:

    model: ChatBotLLM
    data_path: str
    data: list[DataPoint]

    def __init__(self, model: BaseLLM, data_path: str, config: Config, **kwargs) -> None:
        self.model = model
        self.data_path = data_path
        self.config = config

        with open(data_path, "r") as f:
            self.data = json.load(f)

    def checkFloat(self, output: float, answer: float, eps: float=1e2):
        return isclose(output, answer, abs_tol=eps)


    def convertToFloatList(self, lst: list) -> list[float]:
        return list(map(lambda x: float(x), lst))
    
    
    def checkOutput(self, output: npt.ArrayLike, answer: npt.ArrayLike, eps: float=1e2) -> float:
        num_correct = np.sum(np.isclose(output, answer, rtol=eps))
        return num_correct == len(answer)
        
    
    def getModelOutput(self, prompt: str, num_responses=1) -> list[str]:
        self.model.clear_chat_history()
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

        model_output = self.model.get_response(
            prompts=[chat_history for _ in range(num_responses)],
            max_new_tokens=self.config["max_new_tokens"],
            temperature=self.config["temperature"],
            top_p=self.config["top_p"],
            min_tokens=self.config["min_tokens"],
            num_return_sequences=1,
        )
        return [out[0] for out in model_output]


    def getParsedModelOutput(self, prompt: str, id: int, num_responses=1) -> list[list[float]] | None:
        model_output = self.getModelOutput(prompt, num_responses)
        parsed_outputs = []
        for i in range(num_responses):
            parsed_output = process_output(model_output[i], id)
            if parsed_output is None:
                parsed_output = []
            parsed_outputs.append(self.convertToFloatList(parsed_output))
        return parsed_outputs
    
    def eval(self) -> float:
        raise NotImplementedError()

    def submit(self) -> list[dict[str, str]]:
        raise NotImplementedError()

