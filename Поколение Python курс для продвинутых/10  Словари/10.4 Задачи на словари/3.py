import re
a = sorted(re.sub(r'[.,;:-?-!/ ]', '', input().lower()))
b = sorted(re.sub(r'[.,;:-?-!/ ]', '', input().lower()))
print('YES' if a==b else 'NO')