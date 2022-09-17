"""
 Подвиг 4. Объявите в программе класс Player (игрок), объекты которого создаются командой:

player = Player(name, old, score)
где name - имя игрока (строка); old - возраст игрока (целое число); score - набранные очки в игре (целое число). В каждом объекте класса Player должны создаваться аналогичные локальные атрибуты: name, old, score.

С объектами класса Player должна работать функция:

bool(player)
которая возвращает True, если число очков больше нуля, и False - в противном случае.

С помощью команды:

lst_in = list(map(str.strip, sys.stdin.readlines()))
считываются строки из входного потока в список строк lst_in. Каждая строка записана в формате:

"имя; возраст; очки"

Например:

Балакирев; 34; 2048
Mediel; 27; 0
Влад; 18; 9012
Nina P; 33; 0

Каждую строку списка lst_in необходимо представить в виде объекта класса Player с соответствующими данными. И из этих объектов сформировать список players.

Отфильтруйте этот список (создайте новый: players_filtered), оставив всех игроков с числом очков больше нуля. Используйте для этого стандартную функцию filter() совместно с функцией bool() языка Python.

P.S. На экран ничего выводить не нужно.

Sample Input:

Балакирев; 34; 2048
Mediel; 27; 0
Влад; 18; 9012
Nina P; 33; 0
Sample Output:

Напишите программу. Тестируется через std
"""
import sys

class Player:

    def __init__(self, name: str, old: int, score: int):
        self.name = name
        self.old = int(old)
        self.score = int(score)

    def __bool__(self):
        return self.score > 0

    def __len__(self):
        return self.score


lst_in = list(map(str.strip, sys.stdin.readlines()))
players = list(map(lambda w: Player(*w.split('; ')), lst_in))
players_filtered = list(filter(lambda l: bool(l),players))
