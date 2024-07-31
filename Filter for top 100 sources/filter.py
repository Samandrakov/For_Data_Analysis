import pandas as pd

# Загрузка данных из первого и второго Excel-файла
file1 = 'Book_initial.xlsx'
file2 = 'Book1.xlsx'

# Чтение данных из первого файла
df1 = pd.read_excel(file1)

# Чтение данных из второго файла
df2 = pd.read_excel(file2)

# Предположим, что столбцы, которые нужно сравнить, называются 'source_link'
column_name = 'source_link'

# Проверка, что столбцы существуют в обоих DataFrame
if column_name not in df1.columns or column_name not in df2.columns:
    raise ValueError(f"Столбец '{column_name}' не найден в одном из файлов.")

# Находим совпадения
common_values = df1[df1[column_name].isin(df2[column_name])]

# Удаляем совпадения из первого файла
df1_filtered = df1[~df1[column_name].isin(df2[column_name])]

# Сохраняем результат в новый файл
output_file = 'filtered_file1.xlsx'
df1_filtered.to_excel(output_file, index=False)

print(f"Совпадения удалены и результат сохранен в {output_file}")

# Выводим список совпадений
print("Совпадения:")
print(common_values)

# Выводим только строки с совпадениями
if not common_values.empty:
    print("Совпадения (только строки с True):")
    print(common_values)
else:
    print("Совпадений не найдено.")
# Сохраняем совпадения в отдельный файл
common_values.to_excel('common_values.xlsx', index=False)
