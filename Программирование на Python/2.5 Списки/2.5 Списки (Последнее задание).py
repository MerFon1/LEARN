#Нужно что бы програма выводила по одному числу
# из тех чисел что поторяються несколько раз в списке
a = [int(i) for i in input().split()]
print('Полученый список', a)
c = []
b = []
print('Отсортированый список', a)
a.sort()

for i in a:
    if  not i in c:
        c.append(i)
    else:
        b.append(i)
print(*set(b))


