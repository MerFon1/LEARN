# считывание строки и разбиение ее по пробелам
lst_in = input().split()
c = 0
for i in lst_in:
    try:
        c += int(i)
    except:
        pass
print(c)