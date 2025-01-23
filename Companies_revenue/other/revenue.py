import pandas as pd
from SPARQLWrapper import SPARQLWrapper, JSON
import time

# Чтение файла xlsx
input_file = 'REV_COM.xlsx'
batch_size = 1  # Размер батча
df = pd.read_excel(input_file)
print(df.columns)  # Вывод названий колонок

output_file = 'output.csv'

# Установка SPARQL-эндпоинта Wikidata
sparql = SPARQLWrapper("https://query.wikidata.org/sparql")


def get_company_revenue(qid):
    # Запрос к Wikidata для получения последней выручки и валюты
    query = f"""
    SELECT ?revenue ?currencyLabel WHERE {{
      wd:{qid} p:P2139 ?statement.
     OPTIONAL {{ ?statement ps:P2139 ?revenue; 
              pq:P2237 ?currency. }}
      SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }}
    }}
    ORDER BY DESC(?revenue)
    LIMIT 1
    """
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    # Извлечение результата
    if results["results"]["bindings"]:
        revenue = results["results"]["bindings"][0]["revenue"]["value"]
        currency = results["results"]["bindings"][0]["currencyLabel"]["value"]
        return revenue, currency
    return None, None


def process_batch(batch_df):
    # Создание списка для хранения результатов
    output_data = []

    for index, row in batch_df.iterrows():
        name = row['name']
        qid = row['qid']

        # Получение выручки и валюты
        revenue, currency = get_company_revenue(qid)

        # Добавление данных в список
        output_data.append({
            'name': name,
            'revenue': revenue,
            'currency': currency
        })

    # Преобразование списка в DataFrame
    batch_output_df = pd.DataFrame(output_data)

    # Сохранение в CSV файл (добавляем к существующему файлу)
    with open(output_file, 'a', newline='', encoding='utf-8') as f:
        batch_output_df.to_csv(f, header=f.tell() == 0, index=False)


# Чтение файла xlsx
df = pd.read_excel(input_file)

# Обработка данных батчами
total_batches = (len(df) + batch_size - 1) // batch_size

for i in range(total_batches):
    start_idx = i * batch_size
    end_idx = start_idx + batch_size
    batch_df = df[start_idx:end_idx]

    print(f"Processing batch {i + 1}/{total_batches}...")
    process_batch(batch_df)

    # Небольшая задержка для предотвращения перегрузки сервера Wikidata
    time.sleep(1)

print("Processing complete.")
