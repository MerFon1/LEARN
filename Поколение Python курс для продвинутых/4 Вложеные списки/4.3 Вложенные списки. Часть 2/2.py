n = int(input())
lst = []
for i in range(1, n+1):
    pl = []
    for j in range(1, i+1):
        pl.append(j)
    lst.append(pl)
print(*lst, sep='\n')