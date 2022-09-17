"""Зодиак
Китайский гороскоп назначает животным годы в 1212-летнем цикле. Один 1212-летний цикл показан в таблице ниже. Таким образом, 20122012 год будет очередным годом дракона.

Год	Животное
20002000	Дракон
20012001	Змея
20022002	Лошадь
20032003	Овца
20042004	Обезьяна
20052005	Петух
20062006	Собака
20072007	Свинья
20082008	Крыса
20092009	Бык
20102010	Тигр
20112011	Заяц
Напишите программу, которая считывает год и отображает название связанного с ним животного. Ваша программа должна корректно работать с любым годом, не только теми, что перечислены в таблице.

Формат входных данных
На вход программе подается одно целое число – год.

Формат выходных данных
Программа должна вывести текст – название животного.

Тестовые данные 🟢
Sample Input 1:

2020
Sample Output 1:

Крыса
Sample Input 2:

1945
Sample Output 2:

Петух
Sample Input 3:

2000
Sample Output 3:

Дракон"""

years = {0: 'Обезьяна',
         1: 'Петух',
         2: 'Собака',
         3: 'Свинья',
         4: 'Крыса',
         5: 'Бык',
         6: 'Тигр',
         7: 'Заяц',
         8: 'Дракон',
         9: 'Змея',
         10: 'Лошадь',
         11: 'Овца'}
print(years[int(input())%12])
