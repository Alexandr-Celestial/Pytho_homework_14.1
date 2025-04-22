from unittest.mock import patch

from _pytest.capture import CaptureFixture

from src.cls_category import Category
from src.cls_product import Product


def test_init(fixture_category: Category) -> None:
    """Тест для проверки корректности инициализации класса Category"""
    assert fixture_category.name == "mobile"
    assert fixture_category.description == "256GB, Серый цвет, 200MP камера"
    assert len(fixture_category.products) == 1
    product = fixture_category.products[0]
    assert product.name == "Iphone 15"
    assert product.price == 210000.0
    assert product.quantity == 8


def test_category_count() -> None:
    """Тест для класса Category, проверяющий подсчет количества категорий"""
    Category.category_count = 0
    Category("mobile", "256GB, Серый цвет, 200MP камера", [])
    assert Category.category_count == 1


def test_product_count() -> None:
    """Тест для класса Product, для подсчета количества продуктов"""
    test_products = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    Category.product_count = 0
    category = Category("mobile", "256GB, Серый цвет, 200MP камера", [])
    category.add_product(test_products)
    assert Category.product_count == 1


def test_add_product() -> None:
    """Тест метода add_product"""
    Category.category_count = 0
    Category.product_count = 0
    with patch("builtins.input", return_value="y"):
        test_product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        test_data_category = Category("mobile", "256GB, Серый цвет, 200MP камера", [])
        test_data_category.add_product(test_product)
        assert Category.category_count == 1
        assert Category.product_count == 1


def test_price_category(capsys: CaptureFixture[str], product_phone: Product) -> None:
    """Тест изменения продукта в категории"""
    category = Category("Категория 1", "Описание 1", [])

    with patch("builtins.input", lambda _: "y"):
        category.add_product(product_phone)
        product_phone.price = 14000
        category.add_product(product_phone)
        read_outr = capsys.readouterr()
        assert read_outr.out == "Product (Iphone 15, 512GB, Gray space, 210000.0, 8)\n"

    with patch("builtins.input", lambda _: "n"):
        category.add_product(product_phone)
        product_phone.price = 10000
        category.add_product(product_phone)
        read_outr = capsys.readouterr()
        assert read_outr.out == ""


def test_str_(fixture_category_1: Category) -> None:
    """Тестирование метода __str__"""
    assert str(fixture_category_1) == "Смартфоны, количество продуктов: 0 шт"


def test_middle_price_empty() -> None:
    """Тестирование метода middle_price с пустым значением"""
    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    result = category_empty.middle_price()
    assert result == 0.0


def test_middle_price_valid() -> None:
    """Тестирование метода middle_price с валидными значениями"""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])
    result = category1.middle_price()
    assert result == 140333.33333333334
