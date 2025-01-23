import pandas as pd
from qids import qids_names

# Словарь с названиями компаний и их QID

# Обратный словарь для поиска названий по QID
qid_to_name = {v: k for k, v in qids_names.items()}

# Загрузка CSV файла с указанием разделителя
df = pd.read_csv('Company_ready_1.csv', delimiter=';')

# Проверка наличия столбца QID;name и его разделение на два столбца
if 'QID;name' in df.columns:
    df[['QID', 'name']] = df['QID;name'].str.split(';', expand=True)
    df.drop(columns=['QID;name'], inplace=True)

# Проверка наличия столбца QID
print("Столбцы в CSV файле:", df.columns)

if 'QID' not in df.columns:
    raise KeyError("Столбец 'QID' отсутствует в CSV файле.")

# Функция для поиска названия компании по QID
def find_company_name(qid):
    return qid_to_name.get(qid, 'Unknown')

# Применение функции к столбцу QID и создание нового столбца name
df['name'] = df['QID'].apply(find_company_name)

# Сохранение результата в новый CSV файл
df.to_csv('updated_file.csv', index=False)
