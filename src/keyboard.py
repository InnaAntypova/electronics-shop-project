from src.item import Item


class MixinLanguage:
    """ Класс Mixin для реализации метода смены клавиатуры"""

    def __init__(self):
        self.__language = 'EN'

    def change_lang(self):
        """ Метод меняет раскладку клавиатуры """
        if self.__language.upper() == 'EN':
            self.__language = 'RU'
            return self

        if self.__language.upper() == 'RU':
            self.__language = 'EN'
            return self

    @property
    def language(self):
        """ Делаем параметр language приватным."""
        return self.__language


class Keyboard(Item, MixinLanguage):
    """ Класс для товара Keyboard в магазине"""

    def __init__(self, name: str, price: int, quantity: int):
        """ Инициализирует экземпляр наследуясь от класса Item и вспомогательного класса Mixin.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :language: язык раскладки клавиатуры. По умолчанию 'EN'."""
        super().__init__(name, price, quantity)
        MixinLanguage.__init__(self)

    def __repr__(self) -> str:
        """ Возвращает строку с отладочной информацией об экземпляре класса"""
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.language})"

    def __str__(self):
        """ Возвращает строку с информацией об экземпляре класса для пользователя"""
        return f"{self.name}"
