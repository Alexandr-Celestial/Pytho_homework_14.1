import pytest

from src.cls_category import Category
from src.cls_product import Product


@pytest.fixture
def fixture_category() -> Category:
    """Фикстура для теста класса Category"""
    test_products = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    return Category("mobile", "256GB, Серый цвет, 200MP камера", [test_products])


def test_init(fixture_category: Category) -> None:
    """Тест для проверки корректности инициализации класса Category"""
    assert fixture_category.name == "mobile"
    assert fixture_category.description == "256GB, Серый цвет, 200MP камера"
    assert fixture_category.products[0].name == "Iphone 15"
    assert fixture_category.products[0].description == "512GB, Gray space"
    assert fixture_category.products[0].price == 210000.0
    assert fixture_category.products[0].quantity == 8


def test_category_count() -> None:
    """Тест для класса Category, проверяющий подсчет количества категорий"""
    Category.category_count = 0
    Category("mobile", "256GB, Серый цвет, 200MP камера", [])
    assert Category.category_count == 1


def test_product_count() -> None:
    """Тест для класса Product, для подсчета количества продуктов"""
    Category.product_count = 0
    test_products = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    Category("mobile", "256GB, Серый цвет, 200MP камера", [test_products])
    assert Category.product_count == 1
