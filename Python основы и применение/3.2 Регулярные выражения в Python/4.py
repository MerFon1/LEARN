"""

"""

import sys
import re

for string in sys.stdin:
    string = string.rstrip()
    pattern = r"\\"
    if re.search(pattern, string):
        print(string)