from typing import Any

from src.cls_category import Category


class IterItem:
    """Класс для итерации товаров одной категории"""

    def __init__(self, category: Category):
        """Инициализация вспомогательного класса"""
        self.category = category
        self.index = 0

    def __iter__(self) -> Any:
        """Переопределение метода iter"""
        self.index = 0
        return self

    def __next__(self) -> str:
        """Переопределение метода next"""
        if self.index < len(self.category.products):
            result = self.category.products[self.index]
            self.index += 1
            return str(result)
        else:
            raise StopIteration
