import re
from collections import Counter


def operations_by_description(data_operations_list, search_line):
    """Функция для сортировки списка по строке в описании"""
    data_by_description = []
    for operation in data_operations_list:
        find_description = re.search(search_line.lower(), operation["description"].lower())
        if find_description != None:
            data_by_description.append(operation)
    return data_by_description


def operations_count_by_category(data_operations_list, operations_category):
    """Функция подсчёта операций по категориям"""
    data_by_count = []
    for operation in data_operations_list:
        if operation["description"] in operations_category:
            data_by_count.append(operation["description"])
        operation_counter = Counter(data_by_count)
    return dict(operation_counter)


transactions = [
    {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Снятие наличных",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    },
    {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Депозит",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    },
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 587085106,
        "state": "EXECUTED",
        "date": "2018-03-23T10:45:06.972075",
        "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Открытие вклада",
        "to": "Счет 41421565395219882431",
    },
]

# print(operations_by_description(data_base, "Перевод организации"))
categories = ["Перевод организации", "Открытие вклада", "Снятие наличных", "Депозит"]
# print(operations_count_by_category(transactions, categories))
# print(operations_by_description(transactions, "перевод"))
