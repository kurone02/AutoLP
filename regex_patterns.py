import re

PATTERN = re.compile(r"(## start solving)([\s\S]*)(## end solving)")
CODE_PATTERN = re.compile(r"(```.*)([\s\S]*)(```[\s\S]*)")
NUMBER_PATTERN = re.compile(r"[+-]?([0-9]*[.])?[0-9]+$")
