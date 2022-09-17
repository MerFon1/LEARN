"""

"""


import sys
import re

for string in sys.stdin:
    string = string.rstrip()
    pattern = r"(\w)\1+"
    string = re.sub(pattern, r"\1", string)
    print(string)
