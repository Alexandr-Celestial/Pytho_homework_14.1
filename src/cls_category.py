from src.cls_product import Product


class Category:
    """Класс категорий"""

    name: str
    description: str
    products: list[Product]

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        """Инициализация экземпляров класса"""
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products)
