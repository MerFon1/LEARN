"""Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.

Выведите одно число – количество вхождений строки t в строку s.

Пример:
s = "abababa"
t = "aba"

Вхождения строки t в строку s:
abababa
abababa
abababa

Sample Input 1:

abababa
aba
Sample Output 1:

3
Sample Input 2:

abababa
abc
Sample Output 2:

0
Sample Input 3:

abc
abc
Sample Output 3:

1
Sample Input 4:

aaaaa
a
Sample Output 4:

5"""

a, b = [str(input()) for i in range(2)]
counter, st, en = 0, 0, len(b)

while en != (len(a)+1):
    x = a.startswith(b, st, en)
    if x == True:
        counter += 1
        st += 1
        en += 1
    else:
        st += 1
        en += 1
print(counter)


