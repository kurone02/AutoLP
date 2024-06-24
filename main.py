from prompt_evaluation import PromptEngineerEvaluation
from prompt_consistency_evaluation import PromptConsistencyEngineerEvaluation
from finetune_evaluation import FineTuneEvaluation
from prompt_tot_evaluation import PromptToT
from llm import BaseLLM, ChatBotLLM, DeepSeekChatLLM
from evaluation import BaseEvaluation
import json
import os
from tqdm import tqdm

import shutil

from utils import read_json, read_txt, save_json, run_parallel

from argparse import ArgumentParser
from multiprocessing import Process

import sys

def generate_submission(config: dict, device: str, data_path: str, save_path: str, **kwargs):
    # Prompt Engineering
    if config["model"] == "deepseek-ai/deepseek-coder-33b-instruct":
        model = DeepSeekChatLLM(
            model_id=config["model"],
            system_prompt=config["system_prompt"],
            device=device
        )
    elif config["technique"].startswith("Prompt"):
        model = ChatBotLLM(
            model_id=config["model"],
            system_prompt=config["system_prompt"],
            device=device
        )
    else:
        model = BaseLLM(
            model_id=config["model"],
            device=device,
        )

    prompt_template = read_txt(config["prompt_template"])

    technique = getattr(sys.modules[__name__], config["technique"])
    eval: BaseEvaluation = technique(
        model=model,
        data_path=data_path,
        config={
            "max_new_tokens": config["max_new_tokens"],
            "temperature": config["temperature"],
            "top_p": config["top_p"],
            "min_tokens": config["min_tokens"]
        },
        prompt_template=prompt_template,
        num_trials=config["num_trials"],
        **config["kwargs"],
        **kwargs
    )
    
    submission = eval.submit()
    submission_format = read_json(data_path)
    
    for idx, task in enumerate(submission_format):
        task["results"] = submission[idx]

    save_json(save_path, submission_format)



def run(args):

    config = read_json(args.config)

    print("=" * 15, "Configuration", "=" * 15)

    print(json.dumps(config, indent=2))

    print("=" * (30 + len("Configuration")))

    is_parallel = config["parallel"]

    if is_parallel:
        print("=" * 15, "Spliting Data", "=" * 15)
        whole_data = read_json(config["data_path"])
        num_cores = len(config["device"])

        parallel_data_path = os.path.abspath(os.path.join(
            config["data_path"],
            os.pardir,
            f"parallel-{num_cores}"
        ))

        if not os.path.exists(parallel_data_path):
            os.mkdir(parallel_data_path)
            
            n = len(whole_data)
            jump = (n + num_cores - 1) // num_cores
            cnt = 0
            for idx in tqdm(range(0, n, jump)):
                partial_data = whole_data[idx:idx+jump]
                new_path = os.path.join(parallel_data_path, f"{cnt}.json")
                save_json(new_path, partial_data)
                cnt += 1
        
        else:
            print("Data have already been splitted! Skipping...")

        print("=" * (30 + len("Spliting Data")))

        if not os.path.exists("parallel_cwd"):
            os.mkdir("parallel_cwd")

        print("=" * 15, "Running", "=" * 15)
        
        fns = [generate_submission for _ in range(num_cores)]
        fns_arg = [
            (config, f"{i}", os.path.join(parallel_data_path, f"{i}.json"), os.path.join(os.getcwd(), "parallel_cwd", f"{i}.json"))
            for i in range(num_cores)
        ]
        run_parallel(fns, fns_arg)

        print("=" * (30 + len("Running")))

        print("=" * 15, "Merging submissions", "=" * 15)
        final_submission = []
        for i in range(num_cores):
            submission = read_json(os.path.join(os.getcwd(), "parallel_cwd", f"{i}.json"))
            final_submission.extend(submission)
        
        save_json(config["save_path"], final_submission)

        print("=" * (30 + len("Merging submissions")))
            
    else:
        print("=" * 15, "Running", "=" * 15)
        generate_submission(config, "0", config["data_path"], config["save_path"])
        print("=" * (30 + len("Running")))

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('-c', '--config', default='config/prompt/default.json')
    args = parser.parse_args()

    run(args)