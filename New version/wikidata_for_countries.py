from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd
import math
import os
import time

# Чтение CSV файла и извлечение QID и имен
df = pd.read_excel('countries_with_qids.xlsx')
qid_name_map = dict(zip(df['QID'], df['name']))

def save_to_excel(data, filename, sheet_name='Sheet1'):
    # Если файла не существует, создаём новый
    if not os.path.isfile(filename):
        df = pd.DataFrame(data)
        df.to_excel(filename, index=False, sheet_name=sheet_name)
    else:
        # Если файл существует, добавляем данные
        df_existing = pd.read_excel(filename, sheet_name=sheet_name)
        df_new = pd.DataFrame(data)
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
        df_combined.to_excel(filename, index=False, sheet_name=sheet_name)

def fetch_data_for_qids(qid_name_map, country_name_map, filename):
    qid_list = list(qid_name_map.keys())
    name_list = list(country_name_map)
    chunk_size = 1  # Измените размер чанка на необходимое значение
    total_chunks = math.ceil(len(qid_list) / chunk_size)

    for chunk_index in range(total_chunks):
        start = chunk_index * chunk_size
        end = start + chunk_size
        chunk_qids = qid_list[start:end]

        values = ' '.join(f'wd:{qid}' for qid in chunk_qids)
        print(values)
        query = f"""
        SELECT ?country ?countryLabel ?capitalLabel ?population ?governmentFormLabel ?officialLanguageLabel ?gdp ?inception WHERE {{
          VALUES ?country {{ {values} }}

          ?country wdt:P31 wd:Q6256;
                   wdt:P36 ?capital;
                   wdt:P1082 ?population;
                   wdt:P122 ?governmentForm;
                   wdt:P37 ?officialLanguage;
                   wdt:P2131 ?gdp;
                   wdt:P571 ?inception.

          SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }}
        }}
        ORDER BY DESC(?inception)
        LIMIT 1
        """

        sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)

        try:
            results = sparql.query().convert()

            data = []
            for result in results["results"]["bindings"]:
                country = result.get("countryLabel", {}).get("value", "N/A")
                capital = result.get("capitalLabel", {}).get("value", "N/A")
                population = result.get("population", {}).get("value", "N/A")
                governmentForm = result.get("governmentFormLabel", {}).get("value", "N/A")
                officialLanguage = result.get("officialLanguageLabel", {}).get("value", "N/A")
                gdp = result.get("gdp", {}).get("value", "N/A")
                inception = result.get("inception", {}).get("value", "N/A")

                data.append({
                    "QID": chunk_qids[0],
                    "Name": qid_name_map[chunk_qids[0]],  # Добавляем имя из карты
                    "Country": country,
                    "Capital": capital,
                    "Population": population,
                    "Government Form": governmentForm,
                    "Official Language": officialLanguage,
                    "GDP": gdp,
                    "Inception Date": inception
                })

            save_to_excel(data, filename, sheet_name='Sheet1')
            print(f"Data for country with QID {chunk_qids[0]} appended to {filename}")

        except Exception as e:
            print(f"An error occurred for chunk {chunk_index + 1}: {e}")

    time.sleep(3)

# Запуск функции для получения данных и сохранения в Excel
fetch_data_for_qids(qid_name_map, ,"country_data_complete.xlsx")
