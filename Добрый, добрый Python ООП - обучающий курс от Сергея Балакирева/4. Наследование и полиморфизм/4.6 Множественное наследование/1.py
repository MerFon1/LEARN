"""Подвиг 4. С помощью множественного наследования удобно описывать принадлежность объектов к нескольким разным группам. Выполним такой пример.



Определите в программе классы в соответствии с их иерархией, представленной на рисунке выше:

Digit, Integer, Float, Positive, Negative

Каждый объект этих классов должен создаваться однотипной командой вида:

obj = Имя_класса(value)
где value - числовое значение. В каждом классе следует делать свою проверку на корректность значения value:

- в классе Digit: value - любое число;
- в классе Integer: value - целое число;
- в классе Float: value - вещественное число;
- в классе Positive: value - положительное число;
- в классе Negative: value - отрицательное число.

Если проверка не проходит, то генерируется исключение командой:

raise TypeError('значение не соответствует типу объекта')
После этого объявите следующие дочерние классы:

PrimeNumber - простые числа; наследуется от классов Integer и Positive;
FloatPositive - наследуется от классов Float и Positive.

Создайте три объекта класса PrimeNumber и пять объектов класса FloatPositive с произвольными допустимыми для них значениями. Сохраните все эти объекты в виде списка digits.

Затем, используя функции isinstance() и filter(), сформируйте следующие списки из указанных объектов:

lst_positive - все объекты, относящиеся к классу Positive;
lst_float - все объекты, относящиеся к классу Float.

P.S. В программе требуется объявить только классы и создать списки. На экран выводить ничего не нужно."""


class Digit:

    def __init__(self, value, type_=(int,float), compare=None):
        self._check(value, type_, compare)
        self.value = value

    @staticmethod
    def _check(value, type_=(int,float), compare=None):
        if compare is None:
            if type(value) not in type_:
                raise TypeError('значение не соответствует типу объекта')
        else:
            if compare == 'p':
                if type(value) not in type_ or value <= 0:
                    raise TypeError('значение не соответствует типу объекта')
            elif compare == 'n':
                if type(value) not in type_ or value >= 0:
                    raise TypeError('значение не соответствует типу объекта')


class Integer(Digit):

    def __init__(self, value):
        self._check(value, type_=(int, ))
        super().__init__(value)


class Float(Digit):

    def __init__(self, value):
        self._check(value, (float, ))
        super().__init__(value)


class Positive(Digit):

    def __init__(self, value):
        self._check(value, compare='p')
        super().__init__(value)


class Negative(Digit):

    def __init__(self, value):
        self._check(value, compare='n')
        super().__init__(value)


class PrimeNumber(Integer, Positive):
    pass

class FloatPositive(Float, Positive):
    pass


digits = [PrimeNumber(3), PrimeNumber(1), PrimeNumber(4), FloatPositive(1.5), FloatPositive(9.2), FloatPositive(6.5),
          FloatPositive(3.5), FloatPositive(8.9)]

lst_positive  = list(filter(lambda x: isinstance(x, Positive), digits))
lst_float = list(filter(lambda x: isinstance(x, Float), digits))
