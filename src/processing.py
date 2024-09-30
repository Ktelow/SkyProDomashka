from typing import Any


def filter_by_state(data: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция фильтрует данные по указанному состоянию"""
    list_stat = []
    for key in data:
        if key.get("state") == state:
            list_stat.append(key)
    return list_stat


def sort_by_date(date_list: list[dict[str, Any]], reversed: bool = True) -> list[dict[str, Any]]:
    """Функция сортировки списка словарей по дате"""
    sorted_list = sorted(date_list, key=lambda x: x["date"], reverse=reversed)
    return sorted_list
