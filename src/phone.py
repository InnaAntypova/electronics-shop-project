from src.item import Item


class Phone(Item):
    """ Класс представляет категорию Phone в магазине. Наследуется от класса Item."""
    def __init__(self, name: str, price: int, quantity: int, number_of_sim: int) -> None:
        """
        Создание экземпляра класса Phone.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param number_of_sim: Количество sim-карт в телефоне
        """
        super().__init__(name, price, quantity)  # Название, цену и количество забираем из родительского класса
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self) -> int:
        """ Делает параметр number_of_sim приватным"""
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        """ Устанавливает параметр name_of_sim после проверки на кол-во"""
        if number_of_sim == 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")
        self.number_of_sim = number_of_sim

    def __repr__(self) -> str:
        """ Возвращает строку с отладочной информацией об экземпляре класса"""
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
