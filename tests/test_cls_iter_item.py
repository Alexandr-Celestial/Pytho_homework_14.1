import pytest

from src.cls_category import Category
from src.cls_iter_item import IterItem


@pytest.mark.parametrize(
    "result",
    [
        ("Samsung Galaxy S23 Ultra,180000.0 руб. Остаток: 5 шт."),
        ("Google Pixel 7 Pro, 90000.0 рую. Остаток: 7 шт."),
        ("Apple iPhone 14 Pro, 120000.0 руб. Остоток: 10 шт."),
    ],
)
def test_iter_item(fixture_category: Category, result: str) -> None:
    """Тест для проверки метода iter"""
    iter_item = IterItem(fixture_category)
    product_str = str(fixture_category.products[0])
    assert product_str in list(iter_item)


def test_nest_item(fixture_category: Category) -> None:
    """Тест для проверки метода next"""
    iter_item = IterItem(fixture_category)
    assert next(iter_item) == str(fixture_category.products[0])
    # assert next(iter_item) == "Samsung Galaxy S23 Ultra,180000.0 руб. Остаток: 5 шт."
    # assert next(iter_item) == "Google Pixel 7 Pro, 90000.0 рую. Остаток: 7 шт."
    # assert next(iter_item) == "Apple iPhone 14 Pro, 120000.0 руб. Остоток: 10 шт."
