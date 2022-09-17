num =str(input())

if len(num)==6:
    if int(num[0])+int(num[1])+int(num[2])==int(num[3])+int(num[4])+int(num[5]):
        print('Счастливый')
    else:
        print('Обычный')
else:
    print('Введён неправильный билет')







