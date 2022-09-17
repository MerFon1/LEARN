import collections
#Пулачаем вводимые данные и создаеём из них список
word = (input('vedi bukve -').lower().split())

print('Полученый список', word)
#Сортируем список
word.sort()

print('Отсортированый список', word)
# C помощью импортированой функции Counter из библиотеки collections
# cоздаём словарь в котором пишеться
# сколько раз повторялось каждое слово из списка word
mword = collections.Counter(word)

print('Новый словь сформированый благодаря collections.Counter()', mword )
#Созртируем словарь что бы ключь-значение выводились без скобок в ново ряду
for key, value in mword.items():
    print(key, value)








