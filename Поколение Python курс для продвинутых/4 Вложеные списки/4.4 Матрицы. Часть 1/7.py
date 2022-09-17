m = int(input())
cv = [[int(i) for i in input().split()] for i in range(m)]
v,p,n,l = [],[],[],[]

for i in range(m):
    for j in range(m):
        if (i < j) and (i < m-1-j):
            v.append(cv[j][i])
        elif i<j and i>m-1-j:
            p.append(cv[j][i])
        elif i>j and i>m-1-j:
            n.append(cv[j][i])
        elif i>j and i<m-1-j:
            l.append(cv[j][i])

print('Верхняя четверть:',sum(l))
print('Правая четверть:',sum(n))
print('Нижняя четверть:',sum(p))
print('Левая четверть:',sum(v))