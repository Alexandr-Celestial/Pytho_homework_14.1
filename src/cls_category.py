from src.cls_product import Product


class Category:
    """Класс категорий"""

    name: str
    description: str
    __products: list[Product]

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str):
        """Инициализация экземпляров класса"""
        self.name = name
        self.description = description
        self.__products = []
        Category.category_count += 1

    def add_product(self, product: Product) -> None:
        """Метод для добавления товаров в категорию"""
        for old_product in self.__products:
            if old_product.name == product.name:
                old_product.quantity += product.quantity
                if old_product.price <= product.price:
                    old_product.price = product.price
                else:
                    answer_input = input("Введите 'y' для подтверждения или 'n' для отмены действия").lower()
                    if answer_input == "y":
                        old_product.price = product.price
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер, который выводит список товаров в виде строки"""
        result = []
        for product in self.__products:
            result.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return "\n".join(result)
