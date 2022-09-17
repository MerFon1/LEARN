"""
Уникальные символы 1
Напишите программу для вывода количества уникальных символов каждого считанного слова без учета регистра.

Формат входных данных
На вход программе в первой строке подается число nn – общее количество слов. Далее идут nn строк с словами.

Формат выходных данных
Программа должна вывести на отдельной строке количество уникальных символов для каждого слова.

Тестовые данные 🟢
Sample Input 1:

3
Тимур
Beegeek
АнанАс
Sample Output 1:

5
4
3
Sample Input 2:

5
абОнемЕнТы
дозировка
военкОмат
ДрУжиНник
ОпПозицИя
Sample Output 2:

8
8
8
7
6
Sample Input 3:

2
прЕвыСокОмнОгОраСсмотРИтельствУюЩиЙ
вОдоГрязетоРфопарАфинОлечЕние
Sample Output 3:

20
16
"""

r = []
for i in range(int(input())):
    r.extend([len(set(input().lower()))])
print(*r, sep='\n')
