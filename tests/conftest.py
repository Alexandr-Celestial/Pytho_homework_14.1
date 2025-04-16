import pytest

from src.cls_category import Category
from src.cls_product import LawnGrass, Product, Smartphone


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


@pytest.fixture
def fisture_smartphone() -> Smartphone:
    """Фикстура для класса Smartphone"""
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def fixture_lawn_grass() -> LawnGrass:
    """Фикстура для класса LawnGrass"""
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def fixture_category_1() -> Category:
    """Фиикстура для Category"""
    return Category("Смартфоны", "Смартфоны, как средство связи", [])
