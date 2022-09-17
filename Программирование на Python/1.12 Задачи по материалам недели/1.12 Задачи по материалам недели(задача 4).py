import math
form = str(input())
if form == ('треугольник'):
    a = int(input())
    b = int(input())
    c = int(input())
    p = ((a + b + c) / 2)
    S = math.sqrt(p * ((p - a) * (p - b) * (p - c)))
    print(float(S))
elif form == ('прямоугольник'):
    a = int(input())
    b = int(input())
    S = (a*b)
    print(float(S))
elif form == ('круг'):
    r = int(input())
    print(3.14 * r ** 2)
