import pytest

from src.generators import filter_by_currency, card_number_generator,transaction_descriptions


def test_filter_by_currency(transactions_list, transactions_complete):
    """Функция, которая тестирует вывод транкзаций по заданной валюте"""
    assert list(filter_by_currency(transactions_list, "USD")) == transactions_complete
    assert list(filter_by_currency("", "USD")) == []
    assert list(filter_by_currency(transactions_list, "EUR")) == []

def test_transactions_descriptions(transactions_list, discriptions_list):
    """Функция, которая тестирует выдачу описаний транзакций"""
    assert list(transaction_descriptions(transactions_list)) == discriptions_list
    assert list(transaction_descriptions("")) == []
    assert list(transaction_descriptions([])) == []


@pytest.mark.parametrize("start, stop, expected", [(1, 2, ["0000 0000 0000 0001"]), (1, 5, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003", "0000 0000 0000 0004"]), (55, 56, ["0000 0000 0000 0055"]), ("", "", [])])
def test_card_number_generator(start, stop, expected):
    """Функция, тестирующая генерацию номеров карт"""
    assert list(card_number_generator(start, stop)) == (expected)