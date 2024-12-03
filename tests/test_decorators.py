import pytest

from src.decorators import log


def test_log():
    """Тест для проверки декоратора"""
    @log()
    def my_test_func(x, y):
        return x + y

    assert my_test_func(1, 2) == 3
    assert my_test_func("a", 2) == "Произошла ошибка"


def test_log_capsys(capsys):
    """Тест для проверки вывода в консоль"""
    @log()
    def my_test_func(a, b):
        return a + b

    my_test_func(1, 2)

    captured = capsys.readouterr()
    assert captured.out == "Функция: my_test_func, результат: 3 - всё ОК\n"
