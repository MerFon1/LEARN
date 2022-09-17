n = int(input())
cv = [[int(i) for i in input().split()] for i in range(n)]
result = []

for i in range(n):
    for j in range(n):
        if i >= j and i <= n-1-j:
            result.append(cv[i][j])
        elif i<=j and i>=n-1-j:
            result.append(cv[i][j])
print(max(result))
