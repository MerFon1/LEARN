n = int(input())
trb = [1,1,1]
if n<=3:
    print(*trb[:n])
else:
    c = 0
    for i in range(n-3):
        el = trb[c:]
        trb.extend([sum(el)])
        c += 1
    print(*trb)
