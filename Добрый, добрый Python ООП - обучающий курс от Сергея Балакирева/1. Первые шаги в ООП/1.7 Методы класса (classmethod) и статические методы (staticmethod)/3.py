"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/9766M0dS1qc

Подвиг 8. Объявите класс CardCheck для проверки корректности информации на пластиковых картах. Этот класс должен иметь следующие методы:

check_card_number(number) - проверяет строку с номером карты и возвращает булево значение True, если номер в верном формате и False - в противном случае. Формат номера следующий: XXXX-XXXX-XXXX-XXXX, где X - любая цифра (от 0 до 9).
check_name(name) - проверяет строку name с именем пользователя карты. Возвращает булево значение True, если имя записано верно и False - в противном случае.

Формат имени: два слова (имя и фамилия) через пробел, записанные заглавными латинскими символами и цифрами. Например, SERGEI BALAKIREV.

Предполагается использовать класс CardCheck следующим образом (эти строчки в программе не писать):

is_number = CardCheck.check_card_number("1234-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI BALAKIREV")
Для проверки допустимых символов в классе должен быть прописан атрибут:

CHARS_FOR_NAME = ascii_lowercase.upper() + digits
Подумайте, как правильнее объявить методы check_card_number и check_name (декораторами @classmethod и @staticmethod).

P.S. В программе только объявить класс. На экран ничего выводить не нужно.
"""


class CardCheck:

    @staticmethod
    def check_card_number(number):
        import re
        pattern = r"^\d{4}-\d{4}-\d{4}-\d{4}$"
        return re.match(pattern, number) is not None

    @staticmethod
    def check_name(name):
        import re
        r = [name==name.upper(),len(name.split())==2]
        r.append(re.match(r"[A-Z]",name) is not None)
        r.extend([i not in name for i in r'<>.,/\?"''[]{}=+_-)(*&^%$#@!№;:'])
        return all(r)



