import pytest
from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, mask_card_number", [("1234567812345678", "1234 56** **** 5678"), ("22442244", None), ("", None)]
)
def test_get_mask_card_number(card_number: str, mask_card_number: str) -> None:
    assert get_mask_card_number(card_number) == mask_card_number


@pytest.mark.parametrize(
    "account_number, mask_account",
    [("12345678123456781234", "**1234"), ("12341234", None), ("bruh", None), ("", None)],
)
def test_get_mask_account(account_number: str, mask_account: str) -> None:
    assert get_mask_account(account_number) == mask_account
