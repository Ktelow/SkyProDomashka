from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_string: str) -> str | None:
    """Функция маскировки карты и счёта"""
    account_data_split = input_string.split()
    try:
        if len(account_data_split[-1]) == 16:
            return f"""{" ".join(account_data_split[:-1])} {get_mask_card_number(account_data_split[-1])}"""
        elif len(account_data_split[-1]) == 20:
            return f"""{account_data_split[0]} {get_mask_account(account_data_split[-1])}"""
        else:
            return None
    except IndexError:
        return None


def get_date(input_string: str) -> str | None:
    """Функция преобразования даты"""
    date_input = input_string.split("T")[0]
    date_formatted = f"""{date_input[-2:]}.{date_input[5:7]}.{date_input[:4]}"""
    number_count = 0
    for d in date_input:
        if d.isdigit() == 1:
            number_count += 1
    if number_count == 8:
        return date_formatted
    else:
        return None
