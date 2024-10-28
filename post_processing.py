from pathlib import Path
import os
import re
import sys
import subprocess
import json
from typing import Callable
from multiprocessing import Process
from tqdm import tqdm
import sympy as sp
from .regex_patterns import CODE_PATTERN, PATTERN

def remove_division_from_inequality(expr):
    if not isinstance(expr, sp.Rel):
        return "The provided expression is not a relational expression."
    
    lhs, rhs = expr.lhs, expr.rhs
    
    denominators = [term.as_numer_denom()[1] for term in (lhs, rhs) if term.as_numer_denom()[1] != 1]
    
    if not denominators:
        return expr
    
    lcm_denom = sp.lcm_list(denominators)
    modified_lhs = sp.Mul(lhs, lcm_denom, evaluate=False).simplify()
    modified_rhs = sp.Mul(rhs, lcm_denom, evaluate=False).simplify()
    
    new_expr = expr.func(modified_lhs, modified_rhs)
    
    return new_expr

def parse_expr(expr: str) -> str:
    return sp.parsing.sympy_parser.parse_expr(expr)

def extract_expr(code: str) -> str:
    expr = code.split("+=")[-1]
    expr = expr.split("#")[0]
    expr = expr.replace("S", "s__")
    expr = expr.replace(",", "_")
    expr = parse_expr(expr)
    return code.split("+=")[0], expr, code.split("#")[-1]

def fix_division(code: str) -> str:
    new_code = []
    for line in code.split('\n'):
        if "/" in line:
            try:
                prefix, inequality, posfix = extract_expr(line)
                result = remove_division_from_inequality(inequality)
                line = " ".join([prefix, '+=', str(result).replace("s__", "S"), '#', posfix])
            except:
                ...
        new_code.append(line)
    return "\n".join(new_code)

def fix_cond(code: str) -> str:
    code = code.replace(" > ", " >= 1 + ")
    code = code.replace(" < ", " <= -1 + ")
    return code

def fix(code: str) -> str:
    code = fix_cond(code)
    code = fix_division(code)
    return code

# def parse(path, format):
#     with open(path, "r") as f:
#         model_output = f.read()

#     match = CODE_PATTERN.findall(model_output)
#     if len(match) > 0:
#         code = match[0][1]
#     elif model_output.endswith("```"):
#         if model_output.startswith("```"):
#             model_output = "'\n'".join(model_output.split('\n')[1:])
#         code = model_output[:-3]
#     else:
#         cutoff = model_output.find("```")
#         code = model_output[:cutoff]
    
#     save_txt(path, fix(code))

#     batcmd = 'timeout 7 ' + sys.executable + f' {path}'

#     id = int(path.name.split('.')[0])
#     answers = list(format[id]["results"].keys())

#     try:
#         shell_output = subprocess.check_output(batcmd, shell=True, stderr=subprocess.PIPE).decode('utf8')

#         match_str = PATTERN.findall(shell_output)
#         code_outputs = match_str[0][1]

#         code_outputs = list(filter(lambda s: len(s) > 0, code_outputs.split('\n')))
#         parsed_output = list(map(parse_number, code_outputs))

#         if len(parsed_output) < len(answers):
#             excess = len(answers) - len(parsed_output)
#             parsed_output.extend([0 for i in range(excess)])
#         elif len(parsed_output) > len(answers):
#             parsed_output = parsed_output[:len(answers)]

#         for i, key in enumerate(answers):
#             format[id]["results"][key] = parsed_output[i]

#     except:
#         for i, key in enumerate(answers):
#             format[id]["results"][key] = str("0.0")
    
    

# format = read_json("./task3_public_data/task3_test_public.json")

# pathlist = Path("./code-run").rglob('*.py')
# errors = []
# for path in tqdm(sorted(pathlist)):
#     parse(path)

# save_json("prediction.json", format)

# print("The number of errors: ", len(errors))

# for error in errors:
#     print(error)