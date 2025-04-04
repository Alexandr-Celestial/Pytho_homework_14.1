import json


def read_json_file():
    """Функция для чтения json-файла"""
    with open("data/products.json", "r", encoding="utf-8") as file_path:
        data = json.load(file_path)
        return data
