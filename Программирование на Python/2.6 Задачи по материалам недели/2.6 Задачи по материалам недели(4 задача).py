"""
Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк. После последней строки матрицы идёт строка, содержащая только строку "end" (без кавычек, см. Sample Input).

Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент находится с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.

Sample Input 1:

9 5 3
0 7 -1
-5 2 9
end
Sample Output 1:

3 21 22
10 6 19
20 16 -1
Sample Input 2:

1
end
Sample Output 2:

4
"""

matx = []

s = input()
while s!='end':
    l = [int(i) for i in s.split()]
    matx.append(l)
    s = input()

out_matx = [[0 for j in range(len(matx[i]))] for i in range(len(matx))]
for i in range(len(matx)):
    for j in range(len(matx[i])):
        if j + 1 == len(matx[i]) and i+1==len(matx):
            out_matx[i][j] = matx[i - 1][j] + matx[0][j] + matx[i][j - 1] + matx[i][0]
        elif j + 1 == len(matx[i]):
            out_matx[i][j] = matx[i-1][j] + matx[i+1][j] + matx[i][j-1] + matx[i][0]
        elif i+1==len(matx):
            out_matx[i][j] = matx[i-1][j] + matx[0][j] + matx[i][j-1] + matx[i][j+1]
        else:
            out_matx[i][j] = matx[i - 1][j] + matx[i + 1][j] + matx[i][j - 1] + matx[i][j + 1]




[print(*i) for i in out_matx]
