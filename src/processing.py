from typing import Any


def filter_by_state(data: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]] | Any:
    """Функция фильтрует данные по указанному состоянию"""
    list_stat = []
    try:
        for key in data:
            if key.get("state") == state:
                list_stat.append(key)
        if list_stat == []:
            return "Неправильно указаны данные"
        else:
            return list_stat
    except AttributeError:
        return "Неправильно указаны данные"


def sort_by_date(date_list: list[dict[str, Any]], reversed: bool = True) -> list[dict[str, Any]] | Any:
    """Функция сортировки списка словарей по дате"""
    sorted_list = sorted(date_list, key=lambda x: x["date"], reverse=reversed)
    if sorted_list == []:
        return "Неправильно указаны данные"
    else:
        return sorted_list
