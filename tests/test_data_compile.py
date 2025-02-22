import pytest

from src.data_compile import operations_by_description, operations_count_by_category


@pytest.mark.parametrize(
    "data, line, expected",
    [
        (
            [
                {"description": "Перевод один"},
                {"description": "Перевод два"},
                {"description": "вклад один"},
                {"description": "вклад два"},
            ],
            "перевод",
            [{"description": "Перевод один"}, {"description": "Перевод два"}],
        ),
        ("", "", []),
    ],
)
def test_operations_by_description(data, line, expected):
    assert operations_by_description(data, line) == expected


@pytest.mark.parametrize(
    "data,category_list, expected",
    [
        (
            [
                {"description": "Перевод"},
                {"description": "Перевод"},
                {"description": "вклад"},
                {"description": "вклад"},
            ],
            ["Перевод", "вклад"],
            {"Перевод": 2, "вклад": 2},
        )
    ],
)
def test_operations_count_by_category(data, category_list, expected):
    assert operations_count_by_category(data, category_list) == expected
