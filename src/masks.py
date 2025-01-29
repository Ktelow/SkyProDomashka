import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("..\\logs\\masks.log", "w", encoding="UTF-8")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str | None:
    """Функция маскировки номера карты"""
    try:

        logger.info(f"Маскируем номер карты: {card_number}")
        if not card_number.isdigit() or len(card_number) != 16:
            logger.info(f"Введён неправильный номер карты. Номер - {card_number}")
            return "Неправильный номер карты"
        else:
            return f"""{card_number[:4]} {card_number[4:6]}{'*' * 2} {'*' * 4} {card_number[12:]}"""
    except Exception as ex:
        logger.error(f"Произошла ошибка: {ex}")
        return ""


def get_mask_account(account_number: str) -> str | None:
    """Функция маскировки номера счёта"""
    try:
        logger.info(f"Маскируем номер счёта: {account_number}")
        if account_number.isdigit() and len(account_number) == 20:
            return f"""{'*' * 2}{account_number[-4::]}"""
        else:
            logger.info(f"Введён неправильный номер счёта. Номер - {account_number}")
            return "Неправильный номер счёта"
    except Exception as ex:
        logger.error(f"Произошла ошибка: {ex}")
        return ""


#print(get_mask_card_number([]))
#print(get_mask_account([]))
