bn = input()
x,y= bn[0],bn[1]

xd = {'a': 0,'b': 1,'c': 2,'d': 3,'e': 4,'f': 5,'g': 6,'h': 7}

yd = {'8':0,'7':1,'6':2,'5':3,'4':4,'3':5,'2':6,'1':7}

doska = [['.' for i in range(8)] for j in range(8)]

for i in range(8):
    for j in range(8):
        if j==xd[x] and i==yd[y]:
            doska[i][j] = 'N'

for i in range(8):
    for j in range(8):
        if ((xd[x]- j) * (yd[y]- i)) == 2 or ((xd[x]- j) * (yd[y]- i)) == -2:
            doska[i][j] = '*'

[print(*i) for i in doska]

