from unittest.mock import mock_open, patch

import pytest

from src.read_json import read_json_file


def test_read_json_file() -> None:
    """Тест успешной работы функции read_json_file"""
    with patch("builtins.open", mock_open(read_data="[{}]")):
        test_read = read_json_file()
        assert test_read == [{}]


def test_read_json_file_value_error() -> None:
    """Тест успешной работы функции read_json_file с обработкой исключения ValueError"""
    test_json_file = '{"key": "value"}'
    with patch("builtins.open", mock_open(read_data=test_json_file)):
        with pytest.raises(ValueError, match="JSON файл должен содержать список") as e:
            read_json_file()
        assert str(e.value) == "JSON файл должен содержать список"
