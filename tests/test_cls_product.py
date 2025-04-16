import pytest

from src.cls_category import Category
from src.cls_product import LawnGrass, Product, Smartphone


def test_init(fixture_product: Product) -> None:
    """Тест для проверки корректности инициализации класса Product"""
    assert fixture_product.name == "mobile"
    assert fixture_product.description == "256GB, Серый цвет, 200MP камера"
    assert fixture_product.price == 180000.0
    assert fixture_product.quantity == 1


def test_price() -> None:
    """Тест для проверки геттера price"""
    prod = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    prod.price = 125
    assert prod.price == 125


def test_new_product() -> None:
    """Тест класс-метода new_product"""
    test_data_dict = Product.new_product(
        {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
    )
    assert isinstance(test_data_dict, Product)


def test_add_prod(fisture_smartphone: Smartphone, fixture_lawn_grass: LawnGrass, fixture_category_1: Category) -> None:
    with pytest.raises(TypeError):
        fisture_smartphone + fixture_lawn_grass
    with pytest.raises(TypeError):
        fixture_category_1.add_product("Not a product")
