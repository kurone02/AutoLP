import re

PATTERN = re.compile(r"(## start solving)([\s\S]*)(## end solving)")
CODE_PATTERN = re.compile(r"^```(?:\w+)?\s*\n(.*?)(?=^```)```", flags=re.MULTILINE | re.DOTALL)
NUMBER_PATTERN = re.compile(r"[+-]?([0-9]*[.])?[0-9]+$")
