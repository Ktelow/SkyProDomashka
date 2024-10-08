# SkyProDomashka

## Описание:
SkyProDomashka - проект по созданию возможного функционала личного кабинета в приложении банка.

## Требования к окружению:
   ```
   Python 3.12+
   ```

## Установка:

1. Клонируйте репозиторий:
    ```
   git clone [https:](https://github.com/Ktelow/SkyProDomashka)
    ```
2. Установите зависимости:
   ```
   pip install -r requirments.txt

3. Создать и активировать виртуальное окружение:
   ```
   python -m venv venv
   venv\Scripts\activate

## Тестирование:
Этот проект тестируется с помощью фреймворк pytest
Для работы с ним необходимо выполнить команду:
   ```
   poetry add --group dev pytest
   ```
И далее можете выполнять тесты с помощью команды:
   ```
   pytest --cov
   ```

## Использование:

Работа с персональными банковскими данными пользователей и предоставление функций для отслеживания операций
