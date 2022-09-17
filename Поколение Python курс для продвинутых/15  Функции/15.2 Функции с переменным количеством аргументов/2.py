"""
Напишите функцию sq_sum(), которая принимает произвольное количество числовых аргументов и возвращает сумму их квадратов.

Примечание 1. Обратите внимание, что функция должна принимать не список, а именно произвольное количество аргументов.

Примечание 2. Следующий программный код:

print(sq_sum())
print(sq_sum(2))
print(sq_sum(1.5, 2.5))
print(sq_sum(1, 2, 3))
print(sq_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
должен выводить:

0
4
8.5
14
385
Примечание 3. Вызывать функцию sq_sum() не нужно, требуется только реализовать.
"""

def sq_sum(*args):
    r = 0
    for i in args:
        r += i**2
    return r