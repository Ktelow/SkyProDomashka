import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card_one(number_card_one: str) -> None:
    assert mask_account_card(number_card_one) == "Visa 1234 12** **** 1432"


def test_mask_account_card_two(number_card_two: str) -> None:
    assert mask_account_card(number_card_two) == "Master Card 9990 99** **** 9999"


def test_mask_account_card(account_number: str) -> None:
    assert mask_account_card(account_number) == "Счет **5000"


def test_mask_account_card_empty() -> None:
    assert mask_account_card("") == None


@pytest.mark.parametrize(
    "date, date_expected",
    [("2020.11.05T16:12:24", "05.11.2020"), ("1958.05.12", "12.05.1958"), ("random text", None), ("", None)],
)
def test_get_date(date: str, date_expected: str) -> None:
    assert get_date(date) == date_expected
