with open('shif.txt') as l:
    for i in l:
        i.strip()
        s = i
        for c in range(len(s)):
            p = ''
            c = 0
            for i in range(len(s)):
                if i==len(s)-1:
                    p = s[:i+1]
                    s = ''
                    break
                if s[i].isalpha() == True:
                    c += 1
                    if c == 2:
                        p = s[:i]
                        s = s[i:]
                        break
            if len(p) < 2:
                print(p, end='')
            else:
                print(p[0] * int(p[1:]), end='')









