"""
from math import sin
d = {'квадрат': lambda x: x ** 2,
     'куб': lambda x: x ** 3,
     'корень': lambda x: x ** 0.5,
     'модуль': lambda x: abs(x),
     'синус': lambda x: sin(x)}

n = int(input())
f = input()
print(d.get(f)(n))
"""

def digits_recursive(n, digits=[]):
    return digits_recursive(n // 10, [n % 10] + digits) if n else digits or [0]

nums = [int(i) for i in input().split()]

result = sorted(nums,key=lambda n: sum(digits_recursive(n)))

print(*result)