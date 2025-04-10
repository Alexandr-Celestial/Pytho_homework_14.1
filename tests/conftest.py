import pytest

from src.cls_category import Category
from src.cls_product import Product


@pytest.fixture
def fixture_product() -> Product:
    """Фикстура для теста класса Product"""
    return Product("mobile", "256GB, Серый цвет, 200MP камера", 180000.0, 1)


@pytest.fixture
def product_phone() -> Product:
    """Фикстура для класса Product"""
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def fixture_category() -> Category:
    """Фикстура для теста класса Category"""
    test_products = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    test_data_category = Category("mobile", "256GB, Серый цвет, 200MP камера", [test_products])
    return test_data_category
