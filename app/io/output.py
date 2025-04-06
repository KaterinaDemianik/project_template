def write_to_console(text):
    """
    Виводить переданий текст у консоль.

    Параметри:
        text (str): Текст, який потрібно вивести.
    """
    print(text)

def write_to_file_builtin(filepath, text):
    """
    Записує переданий текст у файл за допомогою вбудованих можливостей пайтона.

    Параметри:
        filepath (str): Шлях до файлу, в який потрібно записати текст.
        text (str): Текст, який потрібно записати у файл.
    """
    with open(filepath, 'w') as file:
        file.write(text)

def write_to_file_pandas(filepath, dataframe):
    """
    Записує переданий DataFrame у файл CSV за допомогою бібліотеки pandas.

    Параметри:
        filepath (str): Шлях до файлу CSV, в який потрібно записати DataFrame.
        dataframe (pd.DataFrame): DataFrame, який потрібно записати у файл.
    """
    dataframe.to_csv(filepath, index=False)