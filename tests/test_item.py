"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def get_item():
    item1 = Item("Смартфон", 10000, 20)
    return item1


def test_repr(get_item):
    assert get_item.__repr__() == "Item('Смартфон', 10000, 20)"


def test_srt(get_item):
    assert get_item.__str__() == 'Смартфон'


def test_calculate_total_price(get_item):
    assert get_item.calculate_total_price() == 200000


def test_apply_discount(get_item):
    Item.pay_rate = 0.7
    assert get_item.apply_discount() == 7000


def test_name(get_item):
    assert get_item.name == "Смартфон"

    get_item.name = "СуперСмартфон"
    assert get_item.name == "СуперСмарт"

    get_item.name = "Смарт"
    assert get_item.name == "Смарт"


def test_string_to_number():
    assert Item.string_to_number('55.05') == 55
    assert Item.string_to_number('55') == 55


def test_add():
    item1 = Item("Смартфон", 10000, 20)
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert item1 + phone1 == 25
