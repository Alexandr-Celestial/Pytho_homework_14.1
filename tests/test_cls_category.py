from unittest.mock import patch

import pytest

from src.cls_category import Category
from src.cls_product import Product


@pytest.fixture
def fixture_category() -> Category:
    """Фикстура для теста класса Category"""
    test_products = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    test_data_category = Category("mobile", "256GB, Серый цвет, 200MP камера")
    test_data_category.add_product(test_products)
    return test_data_category


def test_init(fixture_category: Category) -> None:
    """Тест для проверки корректности инициализации класса Category"""
    assert fixture_category.name == "mobile"
    assert fixture_category.description == "256GB, Серый цвет, 200MP камера"
    assert fixture_category.products == "Iphone 15, 210000.0 руб. Остаток: 8 шт."


def test_category_count() -> None:
    """Тест для класса Category, проверяющий подсчет количества категорий"""
    Category.category_count = 0
    Category("mobile", "256GB, Серый цвет, 200MP камера")
    assert Category.category_count == 1


def test_product_count() -> None:
    """Тест для класса Product, для подсчета количества продуктов"""
    test_products = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    Category.product_count = 0
    Category("mobile", "256GB, Серый цвет, 200MP камера").add_product(test_products)
    assert Category.product_count == 1


def test_add_product() -> None:
    """Тест метода add_product"""
    Category.category_count = 0
    Category.product_count = 0
    with patch("builtins.input", return_value="y"):
        test_product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        test_data_category = Category("mobile", "256GB, Серый цвет, 200MP камера")
        test_data_category.add_product(test_product)
        assert Category.category_count == 1
        assert Category.product_count == 1
