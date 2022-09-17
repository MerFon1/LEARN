"""
Почтовый индекс в Латверии имеет вид: LetterLetterNumber_NumberLetterLetter, где Letter – заглавная буква английского алфавита, Number – число от 00 до 9999 (включительно).

Напишите функцию generate_index(), которая с помощью модуля random генерирует и возвращает случайный корректный почтовый индекс Латверии.

Примечание 1. Пример правильного (неправильного) индекса Латверии:

AB23_56VG          # правильный
V3F_231GT          # неправильный
Примечание 2. Обратите внимание на символ _ в почтовом индексе.

Примечание 3. Вызывать функцию generate_index() не нужно, требуется только реализовать.
"""

def generate_index():
    import random
    s = [chr(random.randrange(65, 90)), chr(random.randrange(65, 90)),
         str(random.randint(0, 99)), '_',
         str(random.randint(0, 99)),
         chr(random.randrange(65, 90)), chr(random.randrange(65, 90))]
    inx = ''
    for i in s:
        inx += i
    return inx