import pandas as pd
import difflib

# Прочитать данные из двух CSV файлов
file1 = 'companiesmarketcap_com_Companies_ranked_by_Market_Cap_CompaniesMarketCap.csv'  # Первый файл с заглавными и строчными буквами
file2 = 'updated_file.csv'  # Второй файл, все названия в нижнем регистре

# Загрузка данных
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# Проверка наличия столбца 'name' в обоих DataFrame
if 'name' not in df1.columns or 'name' not in df2.columns:
    raise ValueError("Столбец 'name' отсутствует в одном из файлов.")

# Приведение названий первого файла к нижнему регистру и удаление лишних пробелов
df1['name_lower'] = df1['name'].str.lower().str.strip()

# Приведение названий второго файла к нижнему регистру и удаление лишних пробелов
df2['name_lower'] = df2['name'].str.lower().str.strip()

# Функция для поиска наиболее подходящего названия
def find_best_match(name, name_list):
    match = difflib.get_close_matches(name, name_list, n=1)
    return match[0] if match else None

# Поиск наиболее подходящих названий
df2['best_match'] = df2['name'].apply(lambda x: find_best_match(x, df1['name'].tolist()))

# Слияние двух DataFrame по названию в нижнем регистре
merged_df = pd.merge(df2, df1[['name_lower', 'name']], left_on='best_match', right_on='name_lower', how='left')

# Замена названий во втором файле на оригинальные названия из первого файла
merged_df['name'] = merged_df['name_y']

# Удаление лишних столбцов
merged_df = merged_df.drop(columns=['name_lower_x', 'name_lower_y', 'name_y'])

# Сохранение результата в новый CSV файл
merged_df.to_csv('name_output224.csv', index=False)

print(merged_df)
