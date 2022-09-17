"""
def mean(*args):
    s = 0
    k = 0
    for i in args:
        if type(i) is float or type(i) is int:
            s += i
            k += 1
    if 0 != (s and k):
        return s/k
    else:
        return 0.0
"""

def greet(n,*args):
    r = 'Hello, '+ n
    for i in range(len(args)):
        r = r + ' and ' + args[i]
    r += '!'
    return r