"""
Дополните приведенный код так, чтобы он объединил содержимое двух словарей dict1 и dict2 по ключам, складывая значения по одному и тому же ключу, в случае, если ключ присутствует в обоих словарях. Результирующий словарь необходимо присвоить переменной result.

Примечание. Выводить содержимое словаря result не нужно.
"""

dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

result = {}

for k1,e1 in dict1.items():
    for k2,e2 in dict2.items():
        if k1 not in dict2:
            result[k1] = e1
        elif k2 not in dict1:
            result[k2] = e2
        elif k1==k2:
            result[k1]=e1+e2