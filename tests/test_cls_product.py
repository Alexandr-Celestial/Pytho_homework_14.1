import pytest

from src.cls_product import Product


@pytest.fixture
def fixture_product() -> Product:
    """Фикстура для теста класса Product"""
    return Product("mobile", "256GB, Серый цвет, 200MP камера", 180000.0, 1)


def test_init(fixture_product: Product) -> None:
    """Тест для проверки корректности инициализации класса Product"""
    assert fixture_product.name == "mobile"
    assert fixture_product.description == "256GB, Серый цвет, 200MP камера"
    assert fixture_product.price == 180000.0
    assert fixture_product.quantity == 1
