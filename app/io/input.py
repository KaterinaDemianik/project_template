import pandas as pd

def read_from_console():
    """
    Зчитує текстовий ввід від користувача через консоль.

    Повертає:
        str: Введений користувачем текст.
    """
    return input("Enter text: ")

def read_from_file_builtin(filepath):
    """
    Зчитує вміст файлу за допомогою вбудованих можливостей пайтона.

    Параметри:
        filepath (str): Шлях до файлу, який потрібно зчитати.

    Повертає:
        str: Вміст файлу у вигляді тексту.
    """
    try:
        with open(filepath, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Помилка: Файл '{filepath}' не знайдено.")
        return ""

def read_from_file_pandas(filepath):
    """
    Зчитує дані з файлу за допомогою бібліотеки pandas.

    Параметри:
        filepath (str): Шлях до файлу, який потрібно зчитати.

    Повертає:
        pd.DataFrame: Дані у вигляді DataFrame, зчитані з файлу.
    """
    try:
        return pd.read_csv(filepath)
    except FileNotFoundError:
        print(f"Помилка: Файл '{filepath}' не знайдено.")
        return pd.DataFrame()