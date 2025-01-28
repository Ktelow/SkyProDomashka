import os
from unittest.mock import patch

from dotenv import load_dotenv

from src.external_api import get_transaction_amount

load_dotenv()
API_KEY = os.getenv("API_KEY")

test_transaction_1 = {
    "id": 41428829,
    "status_code": 200,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {"amount": "4", "currency": {"name": "USD", "code": "USD"}},
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560",
}


def test_get_transaction_amount_RUB():
    """Функция для проверки с рублём"""
    assert get_transaction_amount({"operationAmount": {"amount": 1, "currency": {"code": "RUB"}}}) == 1.0


@patch("requests.get")
def test_patch_get_transaction_amount(mock_get):
    """Функция для проверки с иностранной валютой"""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 8.00}
    assert get_transaction_amount(test_transaction_1) == 8.00
