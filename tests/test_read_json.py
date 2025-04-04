from unittest.mock import mock_open, patch

from src.read_json import read_json_file


def test_read_json_file() -> None:
    """Тест успешной работы функции read_json_file"""
    with patch("builtins.open", mock_open(read_data="[{}]")):
        test_read = read_json_file()
        assert test_read == [{}]
