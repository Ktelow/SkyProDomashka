import pytest

@pytest.fixture
def number_card_one():
    return "Visa 1234123412431432"

@pytest.fixture
def number_card_two():
    return "Master Card 9990999009909999"

@pytest.fixture
def account_number():
    return "Счет 22550255909012345000"

