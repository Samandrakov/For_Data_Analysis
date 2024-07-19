import pandas as pd
from name import name

# Чтение первого Excel файла и CSV файла
df_export = pd.read_excel(f"{name}.xlsx")
df_nerc = pd.read_csv("sqllab_untitled_query_1_20240430T122020.csv")

# Первое объединение
merged_data_first = pd.merge(df_export, df_nerc[['title', 'value']], on="title", how="left")

# Чтение второго CSV файла
df_second_csv = pd.read_csv("sqllab_untitled_query_1_20240430T122815.csv")

# Второе объединение
merged_data_second = pd.merge(merged_data_first, df_second_csv[['title', 'value']], on="title", how="left")

# Сохранение объединенных данных в Excel
merged_data_second.to_excel(f"merged_data_with_2.xlsx", index=False)
