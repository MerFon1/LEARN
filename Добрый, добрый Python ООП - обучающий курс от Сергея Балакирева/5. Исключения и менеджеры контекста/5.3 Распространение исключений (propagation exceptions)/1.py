def input_int_numbers():
    nums = input().split()
    result = []
    for i in nums:
        try:
            result.append(int(i))
        except ValueError:
            raise TypeError('все числа должны быть целыми')
    print(*result)

while True:
    try:
        input_int_numbers()
    except:
        continue
    else:
        break
