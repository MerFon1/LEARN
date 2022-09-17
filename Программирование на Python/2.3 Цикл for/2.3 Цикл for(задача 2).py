a = int(input())
b = int(input())
suma = 0
numbers = 0
for i in range(a, b+1):
    if i % 3 == 0:
        suma = suma + i
        numbers += 1
print(suma/numbers)



