"""
Три слова
На вход программе подается строка, состоящая из трех слов. Верно ли, что для записи всех трех слов был использован один и тот же набор букв?

Формат входных данных
На вход программе подается строка, состоящая из трех слов.

Формат выходных данных
Программа должна вывести YES, если для записи всех трех слов был использован один и тот же набор букв и NO в противном случае.

Тестовые данные 🟢
Sample Input 1:

автор товар отвар
Sample Output 1:

YES
Sample Input 2:

шарада баллада услада
Sample Output 2:

NO
Sample Input 3:

сорт торс трос
Sample Output 3:

YES
Sample Input 4:

клоун кулон уклон
Sample Output 4:

YES
"""

a, b, c = input().split()
if set(a) == set(b) == set(c):
    print('YES')
else:
    print('NO')



