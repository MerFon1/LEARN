"""
Анаграммы 1
Анаграмма – слово (словосочетание), образованное путём перестановки букв, составляющих другое слово (или словосочетание). Например, английские слова evil и live – это анаграммы.

На вход программе подаются два слова. Напишите программу, которая определяет, являются ли они анаграммами.

Формат входных данных
На вход программе подаются два слова, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести YES если слова являются анаграммами и NO в противном случае.

Тестовые данные 🟢
Sample Input 1:

thing
night
Sample Output 1:

YES
Sample Input 2:

cat
rat
Sample Output 2:

NO
Sample Input 3:

tea
eat
Sample Output 3:

YES
"""

" 1 ВАРИАНТ РЕШЕНИЯ "
a = input()
b = input()
d_a = {}
d_b= {}
for i in a:
    d_a[i] = a.count(i)

for i in b:
    d_b[i] = b.count(i)

print('YES' if d_a==d_b else 'NO')

" 2 ВАРИАНТ РЕШЕНИЯ "

a = sorted([i for  i in input()])
b = sorted([i for  i in input()])
print('YES' if a==b else 'NO')


