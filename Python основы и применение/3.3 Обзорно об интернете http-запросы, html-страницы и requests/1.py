"""

"""

import requests as req

a = req.get(input())
b = input()
print(a.text)
try:
    if a.text.split('"')[1] is None or req.get(a.text.split('"')[1]).text is None or b is None:
        print('No')
    elif req.get(a.text.split('"')[1]).text.split('"')[1] == b:
        print('Yes')
    else:
        print('No')
except:
    print('No')
