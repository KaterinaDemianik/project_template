import pandas as pd
from app.io.input import read_from_console, read_from_file_builtin, read_from_file_pandas
from app.io.output import write_to_console, write_to_file_builtin, write_to_file_pandas

def main():
    user_input = read_from_console()
    write_to_console(f"Введено з консолі: {user_input}")
    write_to_file_builtin('data/output_from_console.txt', user_input)
    df_from_console = pd.DataFrame([{'text': user_input}])
    write_to_file_pandas('data/output_from_console_pandas.csv', df_from_console)

    file_content_builtin = read_from_file_builtin('data/input_builtin.txt')
    write_to_console(f"Зчитано з файлу (builtin): {file_content_builtin}")
    write_to_file_builtin('data/output_from_builtin.txt', file_content_builtin)
    df_from_builtin = pd.DataFrame([{'text': file_content_builtin}])
    write_to_file_pandas('data/output_from_builtin_pandas.csv', df_from_builtin)

    file_content_pandas = read_from_file_pandas('data/input_pandas.csv')
    write_to_console(f"Зчитано з файлу (pandas):\n{file_content_pandas}")
    write_to_file_builtin('data/output_from_pandas_builtin.txt', file_content_pandas.to_string())
    write_to_file_pandas('data/output_from_pandas.csv', file_content_pandas)

if __name__ == "__main__":
    main()
