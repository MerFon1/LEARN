"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/HPgJtLb2NV8

Подвиг 10 (на повторение). Объявите класс EmailValidator для проверки корректности email-адреса. Необходимо запретить создание объектов этого класса: при создании экземпляров должно возвращаться значение None, например:

em = EmailValidator() # None
В самом классе реализовать следующие методы класса (@classmethod):

check_email(cls, email) - возвращает True, если email записан верно и False - в противном случае;
get_random_email(cls) - для генерации случайного email-адреса по формату: xxxxxxx...xxx@gmail.com, где x - любой допустимый символ в email (латинский буквы, цифры, символ подчеркивания и точка).

Корректность строки email определяется по следующим критериям:

- допустимые символы: латинский алфавит, цифры, символы подчеркивания, точки и собачка @ (одна);
- длина email до символа @ не должна превышать 100 (сто включительно);
- длина email после символа @ не должна быть больше 50 (включительно);
- после символа @ обязательно должна идти хотя бы одна точка;
- не должно быть двух точек подряд.

Также в классе нужно реализовать приватный статический метод класса:

is_email_str(email) - для проверки типа переменной email, если строка, то возвращается значение True, иначе - False.

Метод is_email_str() следует использовать в методе check_email() перед проверкой корректности email. Если параметр email не является строкой, то check_email() возвращает False.

Пример использования класса EmailValidator (эти строчки в программе писать не нужно):

res = EmailValidator.check_email("sc_lib@list.ru") # True
res = EmailValidator.check_email("sc_lib@list_ru") # False
P.S. В программе требуется объявить только класс. На экран ничего выводить не нужно.
"""

class EmailValidator:
    import random
    CORECT_SING= ' '.join("abcdefghijklmnopqrstuvwxyz0123456789._").split()

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def check_email(cls, email):
        if cls.__is_email_str(email):
            if all([i in cls.CORECT_SING or i == "@" for  i in email]):
                if '..' not in email:
                    if email.count('@')==1:
                        if len(email.split('@')[0]) <= 100:
                            if len(email.split('@')[1]) <= 50:
                                if '.' in email.split('@')[1]:
                                    return True
        return False

    @classmethod
    def get_random_email(cls):
        res = ''
        while cls.check_email(res)!=True:
            res = ''
            for i in range(cls.random.randint(1,100)):
                res += cls.random.choice(cls.CORECT_SING)
            res += '@gmail.com'
        return res

    @staticmethod
    def __is_email_str(email):
        return type(email)==str

r = EmailValidator()
print(r is None)