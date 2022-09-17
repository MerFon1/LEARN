"""

"""


class FloatValidator:

    def __init__(self, min_value, max_value):
        self._min_value = min_value
        self._max_value = max_value

    def __call__(self, value, *args, **kwargs):
        if type(value) != float or value < self._min_value or value > self._max_value:
            raise ValueError('значение не прошло валидацию')


class IntegerValidator:

    def __init__(self, min_value, max_value):
        self._min_value = min_value
        self._max_value = max_value

    def __call__(self, value, *args, **kwargs):
        if type(value) != int or value < self._min_value or value > self._max_value:
            raise ValueError('значение не прошло валидацию')


def is_valid(lst, validators):
    result = []
    for i in lst:
        c = 0
        for j in validators:
            try:
                j(i)
            except:
                pass
            else:
                c += 1
        if c>0:
            result.append(i)
    return result
