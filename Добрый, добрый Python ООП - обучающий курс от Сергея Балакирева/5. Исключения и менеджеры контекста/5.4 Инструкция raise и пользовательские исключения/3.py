"""

"""


class DateError(Exception):
    pass


class DateString:

    def __init__(self, date_string):
        date_string = date_string.split('.')
        self.__check_data(date_string)
        self.date = date_string

    def __check_data(self, date):
        if len(date) == 3:
            if all([i.isdigit() for i in date]):
                d, m, y = date
                if 1 <= int(d) <= 31 and 1 <= int(m) <= 12 and 1 <= int(y) <= 3000:
                    return True
        raise DateError("Неверный формат даты")

    def __str__(self):
        d, m, y = self.date
        d, m, y = int(d), int(m), int(y)
        return f"{d:0>2}.{m:0>2}.{y:0>4}"


date_string = input()
try:
    date = DateString(date_string)
    print(date)
except DateError:
    print("Неверный формат даты")