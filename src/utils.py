import json
import logging
from json import JSONDecodeError
from typing import Any

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("..\\logs\\utils.log", "w", encoding="UTF-8")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_operations_data(path: str) -> Any:
    """Функция преобразования json файла"""
    try:
        logger.info(f"Получаем данные из файла: {path}")
        with open(path, encoding="utf-8") as f:
            try:
                logger.info("Получаем список транзакций")
                data_json = json.load(f)
            except JSONDecodeError as er:
                logger.error(f"Ошибка с декодированием файла JSON - {er}")
                print("Ошибка декодирования файла")
                return []
        return data_json
    except FileNotFoundError as er:
        logger.error(f"Ошибка с поиском файла - {er}")
        print("Файл не найден")
        return []


# if __name__ == "__main__":
# path = "..//data/operations.json"
# print(get_operations_data(path)[1])
