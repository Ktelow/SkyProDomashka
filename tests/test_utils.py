from unittest.mock import patch

from src.utils import get_operations_data


def test_invalid_data_get_operations_data():
    """Функция проверки с неправильными данными"""
    assert get_operations_data("") == []
    assert get_operations_data("..//randomfile") == []
    assert get_operations_data(1) == []


@patch("json.load")
def test_patch_get_operations_data(mock_get):
    "patch функция с проверкой функции открытия файла"
    mock_get.return_value = FileNotFoundError
    assert get_operations_data("..//data/operations.json") == []
