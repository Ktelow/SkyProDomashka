from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_string: str) -> str | None:
    """Функция маскировки карты и счёта"""
    account_data_split = input_string.split()
    if len(account_data_split[-1]) == 16:
        return f"""{" ".join(account_data_split[:-1])} {get_mask_card_number(account_data_split[-1])}"""
    elif len(account_data_split[-1]) == 20:
        return f"""{account_data_split[0]} {get_mask_account(account_data_split[-1])}"""
    else:
        return None


def get_date(input_string: str) -> str | None:
    """Функция преобразования даты"""
    date_input = input_string.split("T")[0]
    date_formatted = f"""{date_input[-2:]}.{date_input[5:7]}.{date_input[:4]}"""
    return date_formatted


print(mask_account_card("Счет 73654108430135874305"))
print(get_date("2002-02-07T02:26:18.671407"))
