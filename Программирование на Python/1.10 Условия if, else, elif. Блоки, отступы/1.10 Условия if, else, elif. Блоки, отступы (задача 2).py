n = int(input())
if 1900<=n<=3000:
    if n % 4 == 0 and not n % 100 == 0 or n % 400 == 0:
        print("Високосный")
    else:
        print("Обычный")
