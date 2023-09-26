"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import Item

@pytest.fixture
def get_item():
    item1 = Item("Смартфон", 10000, 20)
    return item1


def test_calculate_total_price(get_item):
    assert get_item.calculate_total_price() == 200000


def test_apply_discount(get_item):
    Item.pay_rate = 0.7
    assert get_item.apply_discount() == 7000
