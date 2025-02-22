import pandas as pd


def read_csv(file_path_csv):
    """Функция, читающая csv файл и возвращающая словарь"""
    try:
        df = pd.read_csv(file_path_csv, sep=";").fillna("")
        data_dict = df.to_dict("records")
        return data_dict
    except Exception:
        return []


def read_excel(file_path_excel):
    """Функция, читающая xlsx файл и возвращающая словарь"""
    try:
        df = pd.read_excel(file_path_excel).fillna("")
        data_dict = df.to_dict("records")
        return data_dict
    except Exception:
        return []


print(read_csv("..//data//transactions.csv")[0:10])
# print(read_excel("..//data//transactions_excel.xlsx")[0:10])
