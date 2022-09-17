r = {}

for i in range(int(input())):
    y = input().split()
    r[y[0]] = y[1]

[print(k,v) for k,v in r.items()]
print('')
[print(k,v) for k,v in r.items() if int(v) >= 4]