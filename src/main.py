import sys

from src.data_compile import operations_by_description
from src.data_read import read_csv, read_excel
from src.processing import filter_by_state, sort_by_date
from src.utils import get_operations_data
from src.widget import get_date, mask_account_card


def currency_filter_json(transaction_list, currency="RUB"):
    """Функция для выборки рублёвых операций файла json"""
    transaction_rub = []
    for transaction in transaction_list:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            transaction_rub.append(transaction)
    return transaction_rub


def currency_filter_csv_excel(transaction_list, currency="RUB"):
    """Функция для выборки рублёвых операций файла csv и xlsx"""
    transaction_rub = []
    for transaction in transaction_list:
        if transaction["currency_code"] == currency:
            transaction_rub.append(transaction)
    return transaction_rub


def main():
    """Основная функция проекта, связывающая его логику и взаимодействующая с пользователем"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    file_choice = input("Пользователь: ")
    path = ""
    transactions_list = []

    if file_choice == "1":
        print("Выбран файл формата JSON")
        path = "..//data//operations.json"
        transactions_list = get_operations_data(path)

    elif file_choice == "2":
        print("Выбран файл формата CSV")
        path = "..//data//transactions.csv"
        transactions_list = read_csv(path)

    elif file_choice == "3":
        print("Выбран файл формата XLSX")
        path = "..//data//transactions_excel.xlsx"
        transactions_list = read_excel(path)

    else:
        print("Выбрана недоступная опция. Завершаю программу")
        sys.exit(0)

    statuses = ["EXECUTED", "CANCELED", "PENDING"]
    transactions_list_status = []
    # def status_choice():
    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        user_status_choice = input("Пользователь:")
        if user_status_choice.upper() in statuses:
            print(f"Операции отфильтрованы по статусу {user_status_choice.upper()}")
            transactions_list_status = filter_by_state(transactions_list, user_status_choice.upper())
            break
        # return transactions_list_status

        else:
            print(f"Статус операции {user_status_choice.upper()} недоступен.")

        # return status_choice()
    # print(status_choice())

    print("Отсортировать операции по дате? Да/Нет")
    user_date_choice = input("Пользователь:")
    if user_date_choice.lower() == "да":
        transactions_list_status = sort_by_date(transactions_list_status)

    print("Отсортировать по возрастанию или по убыванию?")
    user_way_choice = input("Пользователь:")
    if user_way_choice.lower() == "по возрастанию" and file_choice == "1":
        transactions_list_status = sorted(transactions_list_status, key=lambda x: x["operationAmount"]["amount"])
    elif user_way_choice.lower() == "по убыванию" and file_choice == "1":
        transactions_list_status = sorted(
            transactions_list_status, key=lambda x: x["operationAmount"]["amount"], reverse=True
        )

    elif user_way_choice.lower() == "по возрастанию" and file_choice == "2" or "3":
        transactions_list_status = sorted(transactions_list_status, key=lambda x: x["amount"])
    elif user_way_choice.lower() == "по убыванию" and file_choice == "2" or "3":
        transactions_list_status = sorted(transactions_list_status, key=lambda x: x["amount"], reverse=True)

    print("Выводить только рублевые транзакции? Да/Нет")
    user_rub_choice = input("Пользователь:")
    if user_rub_choice.lower() == "да" and file_choice == "1":
        transactions_list_status = currency_filter_json(transactions_list_status)
    elif user_rub_choice.lower() == "да" and file_choice == "2" or "3":
        transactions_list_status = currency_filter_csv_excel(transactions_list_status)

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    user_word_choice = input("Пользователь:")
    if user_word_choice.lower() == "да":
        word_choice = input("Введите слово:")
        transactions_list_status = operations_by_description(transactions_list_status, word_choice)

    if transactions_list_status == []:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

    elif file_choice == "1":
        print(f"Всего банковских операций в выборке: {len(transactions_list_status)}")
        for operation in transactions_list_status:
            print(f'{get_date(operation["date"])} {operation["description"]}')
            if "перевод" in operation["description"].lower():
                print(f'{mask_account_card(operation["from"])} -> {mask_account_card(operation["to"])}')
            else:
                print(f'{mask_account_card(operation["to"])}')
            print(
                f'Сумма: {operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}'
            )

    elif file_choice == "2" or "3":
        print(f"Всего банковских операций в выборке: {len(transactions_list_status)}")
        for operation in transactions_list_status:
            print(f'{get_date(operation["date"])} {operation["description"]}')
            if "перевод" in operation["description"].lower():
                print(f'{mask_account_card(operation["from"])} -> {mask_account_card(operation["to"])}')
            else:
                print(f'{mask_account_card(operation["to"])}')
            print(f"Сумма: {operation["amount"]} {operation["currency_code"]}")


print(main())
