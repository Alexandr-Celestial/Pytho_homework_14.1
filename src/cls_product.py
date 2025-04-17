from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """Базовый абстрактный класс"""

    @abstractmethod
    def new_product(self, data_product: dict) -> "Product": ...

    """Инициализация абстрактного класса"""


class MixinLog:
    """Класс-миксин"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализация класса-миксин"""
        name_cls = self.__class__.__name__
        print(f"{name_cls} ({name}, {description}, {price}, {quantity})")


class Product(BaseProduct, MixinLog):
    """Класс продукта"""

    __slots__ = ("name", "description", "__price", "quantity")
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализация экземпляров класса"""
        MixinLog.__init__(self, name, description, price, quantity)
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, data_product: dict) -> "Product":
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

    def __str__(self) -> str:
        """Переопределение метода str"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> float:
        """Переопределение метода add"""
        if type(self) == type(other):
            return float(self.quantity * self.__price + other.quantity * other.price)
        raise TypeError("Ошибка сложения")


class Smartphone(Product):
    """Класс Смартфоны"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс Трава газонная"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
