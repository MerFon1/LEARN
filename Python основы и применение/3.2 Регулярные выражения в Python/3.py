"""

"""

import sys
import re

for string in sys.stdin:
    string = string.rstrip()
    pattern = r"z[0-9 a-z A-Z]{3}z"
    if re.search(pattern, string):
        print(string)
