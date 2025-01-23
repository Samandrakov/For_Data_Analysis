import pandas as pd

# Путь к вашему файлу Excel
file_path = 'qids_refactored.xlsx'  # замените на реальное имя вашего файла

# Загрузка файла Excel
df = pd.read_excel(file_path)

# Предполагая, что названия находятся в первом столбце (index 0)
column_name = df.columns[0]  # или укажите явно имя столбца, например: 'Names'

# Удаление начальных пробелов в строках в указанном столбце
df[column_name] = df[column_name].str.lstrip()

# Сохранение изменений в новый файл Excel
cleaned_file_path = 'cleaned_excel_file.xlsx'
df.to_excel(cleaned_file_path, index=False)

print(f"Файл с удаленными пробелами сохранен как {cleaned_file_path}")
