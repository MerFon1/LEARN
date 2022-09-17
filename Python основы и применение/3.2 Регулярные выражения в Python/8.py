"""

"""


import sys
import re

for string in sys.stdin:
    string = string.rstrip()
    pattern = r"\b(\w{1})(\w{1})(\w*)\b"
    string = re.sub(pattern, r"\2\1\3", string)
    print(string)