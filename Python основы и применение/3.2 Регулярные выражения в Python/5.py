"""

"""

import sys
import re

for string in sys.stdin:
    string = string.rstrip()
    pattern = r"\b(\w+)\1\b"
    if re.search(pattern, string):
        print(string)