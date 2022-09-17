"""
Встречалось ли число раньше?
На вход программе подается строка текста, содержащая числа. Для каждого числа выведите слово YES (в отдельной строке), если это число ранее встречалось в последовательности или NO, если не встречалось.

Формат входных данных
На вход программе подается строка текста, содержащая числа, разделенные символом пробела.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Ведущие нули в числах должны игнорироваться.

Тестовые данные 🟢
Sample Input 1:

1 1 2 2 5 5 5 5 6 7 8
Sample Output 1:

NO
YES
NO
YES
NO
YES
YES
YES
NO
NO
NO
Sample Input 2:

10 5 48 6 38 1
Sample Output 2:

NO
NO
NO
NO
NO
NO
Sample Input 3:

1 1 1 1 1 1 1 1 1
Sample Output 3:

NO
YES
YES
YES
YES
YES
YES
YES
YES
Sample Input 4:

1 2 3 002 03 4 5 05
Sample Output 4:

NO
NO
NO
YES
YES
NO
NO
YES
"""

nums = [int(i) for i in input().split()]
r = set()
chek = lambda el,s: print('YES') if i in r else print('NO')
for i in nums:
    chek(i,nums)
    r.add(i)
