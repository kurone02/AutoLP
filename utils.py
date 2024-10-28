import os
import re
import sys
import subprocess
import json
from collections import Counter
from typing import Callable
from multiprocessing import Process
from .post_processing import fix
from .regex_patterns import *

def read_json(file_path: str) -> dict:
    with open(file_path, "r") as f:
        data = json.load(f)
    return data

def save_json(file_path: str, data: any) -> None:
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

def read_txt(file_path: str) -> str:
    with open(file_path, "r") as f:
        data = f.read()
    return data

def save_txt(file_path: str, data: str) -> None:
    """Save data to a text file"""
    with open(file_path, "w") as f:
        f.write(data)

def parse_number(s: str):
    """Extract the last number from a string"""
    matches = NUMBER_PATTERN.finditer(s)
    matches = list(matches)
    if len(matches) == 0:
        return "0.0"
    return matches[-1].group(0)

def parse_code(markdown: str):
    """Extract the last code block from the markdown content"""
    matches = CODE_PATTERN.finditer(markdown)
    matches = list(matches)
    assert len(matches) > 0
    assert len(matches[-1].groups()) == 1
    return matches[-1].group(1)

def process_output(output: str, id: int):
    try:
        first_pattern = """from pulp import *"""
        idx = output.find(first_pattern)
        output = output[idx:]
        
        last_pattern = """print("## end solving")"""
        idx = output.find(last_pattern)
        output = output[:idx+len(last_pattern)]
                    
        match = CODE_PATTERN.findall(output)
        if len(match) > 0:
            code = match[0][1]
        else:
            if output.startswith("```"):
                output = "'\n'".join(output.split('\n')[1:])
            if output.endswith("```"):
                code = output[:-3]
            else:
                code = output

        code = fix(code)
        
        code_path = f'code-run/{id}.py'

        with open(code_path, 'w') as fout:
            fout.write(code)

        batcmd = 'timeout 7 ' + sys.executable + f' {code_path}'
        shell_output = subprocess.check_output(batcmd, shell=True, stderr=subprocess.PIPE).decode('utf8')

        match_str = PATTERN.findall(shell_output)
        code_outputs = match_str[0][1]

        code_outputs = list(filter(lambda s: len(s) > 0, code_outputs.split('\n')))
        parsed_answers = list(map(parse_number, code_outputs))

        return parsed_answers

    except Exception as e:
        return None

def ensemble(list_parsed_output: list[tuple[float]]) -> list[float]:
    counter = Counter(map(lambda x: tuple(x), list_parsed_output))
    return list(counter.most_common()[0][0])

def run_parallel(fns: list[Callable], fns_arg: list[tuple]):
    proc = []
    for fn, args in zip(fns, fns_arg):
        p = Process(target=fn, args=args)
        p.start()
        proc.append(p)

    for p in proc:
        p.join()
        
        
def convert_score(s: str) -> int:
    try:
        return int(s) 
    except:
        return 5
    
def process_token(token_ids, logits):
    for i in range(15, 25):
        logits[i] += 10000
    return logits