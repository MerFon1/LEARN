n = [int(i) for i in  input().split()]
resu = []
for i in range(len(n)-1):
    if i == n[-1]:
        r = n[i-1]+n[0]
        resu.append(r)
    else:
        r = n[i -1] +n[i+1]
        resu.append(r)
print(resu)


