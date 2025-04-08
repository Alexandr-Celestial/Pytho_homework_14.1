from typing import Self


class Product:
    """Класс продукта"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализация экземпляров класса"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, data_product: dict) -> Self:
        """Класс-метод принимающий на вход параметры товара в словаре и возвращает созданный объект класса Product"""
        return cls(**data_product)

    @property
    def price(self) -> float:
        """Геттер для возврата значение приватного атрибута цены"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price
