lst_in = input().split()
lst_out = []
for i in lst_in:
    try:
        lst_out.append(int(i))
    except:
        try:
            lst_out.append(float(i))
        except:
            lst_out.append(i)



