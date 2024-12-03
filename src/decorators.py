import os
from functools import wraps


def log(filename=None):
    """Декоратор, который создаёт файл с заданным именем и выдаёт надпись об успехе или причину ошибки"""

    def my_dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename is not None:
                    os.makedirs(os.path.dirname(filename), exist_ok=True)
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"Функция: {func.__name__}, результат: {result} - всё ОК")
                else:
                    print(f"Функция: {func.__name__}, результат: {result} - всё ОК")

            except Exception as er:
                result = "Произошла ошибка"
                print(f"{func.__name__} - ERROR: {er} with inputs: {args}, {kwargs}\n")
            return result

        return wrapper

    return my_dec
