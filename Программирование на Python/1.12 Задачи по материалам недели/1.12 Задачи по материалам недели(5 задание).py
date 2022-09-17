#Напишите программу, которая получает на вход три целых числа, по одному числу в строке, и выводит на консоль в три строки сначала максимальное, потом минимальное, после чего оставшееся число.

#На ввод могут подаваться и повторяющиеся числа.

#Sample Input 1:

#8
#2
#14
#Sample Output 1:

#14
#2
#8
#Sample Input 2:

#23
#23
#21
#Sample Output 2:

#23
#21
#23

spi = [int(input()) for i in range(3)]
print(spi)

print(max(spi))
spi.remove(max(spi))

min_spi = min(spi)
spi.remove(min(spi))

print(min_spi)
print(*spi)
