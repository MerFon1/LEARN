"""
Дополните приведенный код, чтобы он вывел сумму наибольшей и наименьшей цифры Decimal числа.

Подсказка
Для отладки кода 🟡
Тестовые данные 🟢
Sample Input 1:

12.1244354689
Sample Output 1:

10
Sample Input 2:

0.1244354689
Sample Output 2:

9
"""
num = input()
res = []
for i in num:
    if i == '.' or i == '-':
        continue
    else:
        res.extend([int(i)])
print(max(res) + min(res))