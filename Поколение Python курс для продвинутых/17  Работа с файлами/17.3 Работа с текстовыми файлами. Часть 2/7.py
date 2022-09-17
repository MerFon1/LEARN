"""
with open('file.txt') as file:
    letters = 0
    words = 0
    lines = len(file.readlines())
    file.seek(0)
    for i in range(lines):
        f = file.readline().strip().split()
        words += len(f)
        for w in f:
            for b in w:
                if b.isalpha():
                    letters += 1
    print(f"Input file contains:\n"
          f"{letters} letters\n"
          f"{words} words\n"
          f"{lines} lines")
"""
from random import choice
with open('first_names.txt') as names, open('last_names.txt') as surnames:
    s = surnames.read().split()
    n = names.read().split()
    for i in range(3):
        print(choice(n), choice(s))







