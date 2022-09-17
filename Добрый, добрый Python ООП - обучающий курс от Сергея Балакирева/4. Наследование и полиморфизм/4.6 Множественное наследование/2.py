"""

"""


class ShopItem:
    ID_SHOP_ITEM = 0

    def __init__(self):
        super().__init__()
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self):
        return self._id


# здесь объявляйте классы ShopGenericView и ShopUserView


class ShopGenericView:

    def __str__(self):
        r = ''
        for k, v in self.__dict__.items():
            r += f"{k}: {v}\n"
        return r

    def __repr__(self):
        r = ''
        for k, v in self.__dict__.items():
            r += f"{k}: {v}\n"
        return r


class ShopUserView:

    def __str__(self):
        r = ''
        for k, v in self.__dict__.items():
            if k != '_id':
                r += f"{k}: {v}\n"
        return r

    def __repr__(self):
        r = ''
        for k, v in self.__dict__.items():
            if k != '_id':
                r += f"{k}: {v}\n"
        return r


class Book(ShopItem, ShopGenericView):
    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year

book = Book('OOP', "balakiev", 2022)
print(book)
