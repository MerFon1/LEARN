A = int(input())
B = int(input())
H = int(input())

if B>=H>=A:
    print('Это нормально')
elif B<H:
    print('Пересып')
elif A>H:
    print('Недосып')