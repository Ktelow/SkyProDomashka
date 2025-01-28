import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_transaction_amount(transaction: dict) -> float:
    """Функция конвертации валюты"""
    amount = 0
    currency_code = transaction["operationAmount"]["currency"]["code"]
    amount_transaction = transaction["operationAmount"]["amount"]
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={'RUB'}&from={currency_code}&amount={amount_transaction}"
    if currency_code != "RUB":
        try:
            payload = {"amount": f"{amount_transaction}", "from": f"{currency_code}", "to": "RUB"}

            headers = {"apikey": f"{API_KEY}"}
            response = requests.get(url, headers=headers, params=payload)
            status_code = response.status_code
            if status_code == 200:
                data_json = response.json()
                amount += data_json["result"]
                return round(amount, 3)
            else:
                print(status_code)
                print(f"Запрос не был успешным. Возможная причина: {response.reason}")
        except requests.exceptions.RequestException:
            print("Ошибка конвертации")
    else:
        amount += float(transaction["operationAmount"]["amount"])
        return amount


transaction = {
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {"amount": "2", "currency": {"name": "USD", "code": "US"}},
}
transaction_amount = get_transaction_amount(transaction)

print(transaction_amount)
