"""Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в каждой строке записана следующая информация:

Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку

Поля внутри строки разделены точкой с запятой, оценки — целые числа.

Напишите программу, которая считывает исходный файл с подобной структурой и для каждого абитуриента записывает его среднюю оценку по трём предметам на отдельной строке, соответствующей этому абитуриенту, в файл с ответом.

Также вычислите средние баллы по математике, физике и русскому языку по всем абитуриентам и добавьте полученные значения, разделённые пробелом, последней строкой в файл с ответом.

В качестве ответа на задание прикрепите полученный файл со средними оценками по каждому ученику и одной строкой со средними оценками по трём предметам.

Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом:

print('First;Second-1 Second-2;Third'.split(';'))
# ['First', 'Second-1 Second-2', 'Third']
Sample Input:

Петров;85;92;78
Сидоров;100;88;94
Иванов;58;72;85
Sample Output:

85.0
94.0
71.666666667
81.0 84.0 85.666666667"""


def lavg(lst):
    result = sum(lst)/len(lst)
    return result

def coun(x):
    if (x*10)%10 == 0:
        return ("%.1f" % x)
    else:
        return ("%.9f" % x)

with open("och.txt", "r", encoding='utf-8') as f:
    c_math = []
    c_fizi = []
    c_ruyaz = []

    for ch in f:
        ch = ch.strip().split(';')
        del ch[0]
        intch = [int(i) for i in ch]
        for i in range(3):
            oc = intch[i]
            if i == 0:
                c_math.append(oc)
            if i == 1:
                c_fizi.append(oc)
            elif i ==2:
                c_ruyaz.append(oc)
        print(coun(lavg(intch)))
    print(coun(lavg(c_math)), coun(lavg(c_fizi)), coun(lavg(c_ruyaz)))



































#with open('srf och.txt') as tf: