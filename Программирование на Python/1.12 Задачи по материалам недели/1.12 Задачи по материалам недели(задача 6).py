n = int(input())
last_n = (n % 10)
two_n = ((n%100) // 10)
if ((0)<=(n)<=(1000)):
    if (n==0):
        print(str(n), 'программистов')
    elif two_n == (1):
        print(str(n), 'программистов')
    elif last_n == (0):
        print(str(n), 'программистов')
    elif last_n == (5):
        print(str(n), 'программистов')
    elif last_n == (6):
        print(str(n), 'программистов')
    elif last_n == (7):
        print(str(n), 'программистов')
    elif last_n == (8):
        print(str(n), 'программистов')
    elif last_n == (9):
        print(str(n), 'программистов')
    elif last_n == (1):
        print(str(n), 'программист')
    elif last_n == ((2) or (3) or (4)):
        print(str(n), 'программиста')
