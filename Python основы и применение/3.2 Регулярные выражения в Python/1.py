# put your python code here
import sys

for line in sys.stdin:
    line = line.rstrip()
    if line.count('cat')>1:
        print(line)
