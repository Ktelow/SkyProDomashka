def get_mask_card_number(card_number: str) -> str | None:
    """Функция маскировки номера карты"""
    if not card_number.isdigit() or len(card_number) != 16:
        return None
    else:
        return f"""{card_number[:4]} {card_number[4:6]}{'*' * 2} {'*' * 4} {card_number[12:]}"""


def get_mask_account(account_number: str) -> str | None:
    """Функция маскировки номера счёта"""
    if account_number.isdigit() and len(account_number) == 20:
        return f"""{'*' * 2}{account_number[-4::]}"""
    else:
        return None
