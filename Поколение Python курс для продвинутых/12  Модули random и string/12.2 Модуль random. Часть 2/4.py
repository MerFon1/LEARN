"""
Напишите программу, которая с помощью модуля random генерирует 100100 случайных номеров лотерейных билетов и выводит их каждый на отдельной строке. Обратите внимание, вы должны придерживаться следующих условий:

номер не может начинаться с нулей;
номер лотерейного билета должен состоять из 77 цифр;
все 100100 лотерейных билетов должны быть различными.
"""

import random
r = set()

while len(r)!=100:
    r.add(random.randint(1000000,9999999))

print(*r, sep='\n')