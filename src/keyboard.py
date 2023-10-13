from src.item import Item


class MixinLanguage:
    """ Класс Mixin для реализации метода смены клавиатуры"""

    def __init__(self):
        self.language = 'EN'

    def change_lang(self):
        """ Метод меняет раскладку клавиатуры """
        if self.language.upper() == 'EN':
            self.language = 'RU'
            return self

        if self.language.upper() == 'RU':
            self.language = 'EN'
            return self

    # def __init__(self):
    #     self.__language = 'EN'
    #
    # @property
    # def language(self):
    #     """ Делаем параметр language приватным."""
    #     return self.__language

    # def change_lang(self):
    #     """ Метод меняет раскладку клавиатуры """
    #     if self.__language.upper() == 'EN':
    #         self.__language = 'RU'
    #         return self
    #
    #     if self.__language.upper() == 'RU':
    #         self.__language = 'EN'
    #         return self


class Keyboard(Item, MixinLanguage):
    """ Класс для товара Keyboard в магазине"""

    def __init__(self, name: str, price: int, quantity: int, language='EN'):
        """ Инициализирует экземпляр наследуясь от класса Item и вспомогательного класса Mixin.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :language: язык раскладки клавиатуры. По умолчанию 'EN'."""
        super().__init__(name, price, quantity)
        self.language = language

    # @property
    # def language(self):
    #     """ Делаем параметр language приватным."""
    #     return self.__language

    def __repr__(self) -> str:
        """ Возвращает строку с отладочной информацией об экземпляре класса"""
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.language})"

