"""

"""
import random

class DataBase:

    def __init__(self,path: str):
        self.path = path
        self.dict_db = {}

    def write(self, record):
        self.dict_db.setdefault(record, [])
        self.dict_db[record].append(record)

    def read(self, pk):
        r = (x for row in self.dict_db.values() for x in row)
        obj = tuple(filter(lambda x: x.pk == pk, r))
        return obj[0] if len(obj) > 0 else None

class Record:

    def __init__(self,fio: str, descr: str, old: int):
        self.pk = random.randint(0,10000)
        self.fio = fio
        self.descr = descr
        self.old = old

    def __eq__(self, other):
        return self.fio == other.fio and self.old == other.old

    def __hash__(self):
        return hash((self.fio.lower(), self.old))

import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))
db = DataBase('database.dt')
for l in lst_in:
    args = list(map(str.strip, l.split(";")))
    args[-1] = int(args[-1])
    db.write(Record(*args))

db22345 = DataBase('123')
r1 = Record('fio', 'descr', 10)
r2 = Record('fio', 'descr', 10)
assert r1.pk != r2.pk, "равные значения атрибута pk у разных объектов класса Record"

db22345.write(r2)
r22 = db22345.read(r2.pk)
assert r22.pk == r2.pk and r22.fio == r2.fio and r22.descr == r2.descr and r22.old == r2.old, "при операциях write и read прочитанный объект имеет неверные значения атрибутов"

assert len(db22345.dict_db) == 1, "неверное число объектов в словаре dict_db"

fio = lst_in[0].split(';')[0].strip()
v = list(db.dict_db.values())
if fio == "Балакирев С.М.":
    assert len(v[0]) == 2 and len(v[1]) == 1 and len(v[2]) == 1 and len(
        v[3]) == 1, "неверно сформирован словарь dict_db"

if fio == "Гейтс Б.":
    assert len(v[0]) == 2 and len(v[1]) == 2 and len(v[2]) == 1 and len(
        v[3]) == 1, "неверно сформирован словарь dict_db"



