
class Item:
    """Класс Item для представления товара"""

    # Переменная на уровне класса для хранения уровня цен
    pay_rate = 0.85

    # Список для хранения экземпляров класса
    all = []

    def __init__(self, item_name, price, quantity_items):
        """ Метод для инициализации класса с атрибутами:
                        item_name - наименование товара,
                        price - цена,
                        quantity_items - количество товара"""
        self.item_name = item_name
        self.price = price
        self.quantity_items = quantity_items
        self.all.append(self)

    def calculate_total_price(self):
        """ Метод возвращает общую стоимость товара"""
        return self.price * self.quantity_items

    def apply_discount(self):
        """ Метод возвращает общую стоимость с учетом скидки"""
        return self.price * self.quantity_items * self.pay_rate
