from unittest.mock import patch

import pandas as pd

from src.data_read import read_csv, read_excel

expected = [
    {
        "id": 650703,
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": 16210.0,
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации",
    }
]


@patch("pandas.read_csv")
def test_read_csv(mock_read):
    """Проверка фиктивного вызова файла с помощью patch"""
    mock_read.return_value = pd.DataFrame(
        {
            "id": [650703],
            "state": ["EXECUTED"],
            "date": ["2023-09-05T11:30:32Z"],
            "amount": [16210.0],
            "currency_name": ["Sol"],
            "currency_code": ["PEN"],
            "from": ["Счет 58803664561298323391"],
            "to": ["Счет 39745660563456619397"],
            "description": ["Перевод организации"],
        }
    )
    assert read_csv("..//data/transactions.csv") == expected


def test_error_read_csv():
    """Проверка вызова ошибки в функции read_csv"""
    assert read_csv("nothing") == []


def test_error_read_excel():
    """Проверка вызова ошибки в функции read_excel"""
    assert read_excel("nothing") == []


@patch("pandas.read_excel")
def test_read_excel(mock_read):
    """Проверка фиктивного вызова файла с помощью patch"""
    mock_read.return_value = pd.DataFrame(
        {
            "id": [650703],
            "state": ["EXECUTED"],
            "date": ["2023-09-05T11:30:32Z"],
            "amount": [16210.0],
            "currency_name": ["Sol"],
            "currency_code": ["PEN"],
            "from": ["Счет 58803664561298323391"],
            "to": ["Счет 39745660563456619397"],
            "description": ["Перевод организации"],
        }
    )
    assert read_excel("..//data/transactions_excel.xlsx") == expected
