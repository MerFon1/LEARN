"""
Тимур и его команда
На летних каникулах Тимур и ученики онлайн-школы BEEGEEK решили отдохнуть. В результате nn учеников школы поехали отдыхать на море, mm учеников съездили в деревню, а kk учеников сходили в горы. Оказалось, что и в деревне, и на море были xx учеников, а в деревне и в горах — yy учеников. Побывать и в горах, и на море не удалось никому.

Напишите программу для определения количества учеников в школе, если никто не смог посетить все три места сразу, а zz учеников писали ДВИ по математике для поступления в МГУ, и никуда не ездили.

Формат входных данных
На вход программе подаются числа n, m, k, x, y, zn,m,k,x,y,z, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести одно число в соответствии с условием задачи.


Тестовые данные 🟢
Номер теста	Входные данные	Выходные данные
1	14
16
5
10
3
2	24
2	25
20
7
8
3
10	51
Sample Input:

14
16
5
10
3
2
Sample Output:

24
"""

#поехали отдыхать на море
n = int(input())

#съездили в деревню
m = int(input())

#сходили в горы
k = int(input())

#и в деревне, и на море были
x = int(input())

#в деревне и в горах
y = int(input())

#писали ДВИ по математике для поступления в МГУ, и никуда не ездили.
z = int(input())

#побывали тольк ов горах
xn = n-x
#побывали только в деревне
myx = (m -x)-y
#побывали только в горах
ky = k-y

#всего учеников
print(ky+myx+xn+z+x+y)