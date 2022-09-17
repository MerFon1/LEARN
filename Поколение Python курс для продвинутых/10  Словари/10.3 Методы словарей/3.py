"""
Дополните приведенный код так, чтобы в переменной result хранился словарь, в котором для каждого символа строки text будет подсчитано количество его вхождений.

Примечание. Выводить содержимое словаря result не нужно.
"""

text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

result = {}
for i in sorted(set(text)):
    result[i] = text.count(i)
