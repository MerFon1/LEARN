"""

"""

import sys
import re

for string in sys.stdin:
    string = string.rstrip()
    pattern = r"\b(a|A)+\b"
    string = re.sub(pattern, 'argh', string, 1)
    print(string)
