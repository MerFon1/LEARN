"""Вам дается текстовый файл, содержащий некоторое количество непустых строк.
На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.

Пример входного файла:
ab
c
dde
ff

﻿Пример выходного файла:
ff
dde
c
ab
"""

text_lst = []
with open('dataset_24465_4.txt') as fi:
    for li in fi:
        lines = li.strip()
        text_lst.append(lines)
text_lst.reverse()
for i in text_lst:
    print(i)
