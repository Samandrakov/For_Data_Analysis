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

def fetch_data_for_qids(qid_name_map, filename):
    qid_list = list(qid_name_map.keys())

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

          OPTIONAL {{ ?country wdt:P36 ?capital. }}
          OPTIONAL {{ ?country wdt:P1082 ?population. }}
          OPTIONAL {{ ?country wdt:P122 ?governmentForm. }}
          OPTIONAL {{ ?country wdt:P37 ?officialLanguage. }}
          OPTIONAL {{ ?country wdt:P2131 ?gdp. }}
          OPTIONAL {{ ?country wdt:P571 ?inception. }}

          SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],ru". }}
        }}
        ORDER BY DESC(?inception)
        """

        sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)

        try:
            results = sparql.query().convert()

            data_map = {}  # Словарь для уникальных данных по каждой стране

            for result in results["results"]["bindings"]:
                country_qid = chunk_qids[0]
                country = result.get("countryLabel", {}).get("value", "N/A")
                capital = result.get("capitalLabel", {}).get("value", "N/A")
                population = result.get("population", {}).get("value", "N/A")
                governmentForm = result.get("governmentFormLabel", {}).get("value", "N/A")
                officialLanguage = result.get("officialLanguageLabel", {}).get("value", None)
                gdp = result.get("gdp", {}).get("value", "N/A")


                # Если страна уже в data_map, добавляем новый язык
                if country_qid in data_map:
                    if officialLanguage and officialLanguage not in data_map[country_qid]["Official Languages"]:
                        data_map[country_qid]["Official Languages"].append(officialLanguage)
                else:
                    # Если страны нет в data_map, добавляем новую запись
                    data_map[country_qid] = {
                        "QID": country_qid,
                        "Name": qid_name_map[country_qid],
                        "Country": country,
                        "Capital": capital,
                        "Population": population,
                        "Government Form": governmentForm,
                        "Official Languages": [officialLanguage] if officialLanguage else [],
                        "GDP": gdp,

                    }

            # Преобразуем языки в строки и добавляем в список данных
            data = []
            for country_data in data_map.values():
                country_data["Official Languages"] = ", ".join(country_data["Official Languages"])
                data.append(country_data)

            save_to_excel(data, filename, sheet_name='Sheet1')
            print(f"Data for chunk {chunk_index + 1} appended to {filename}")

        except Exception as e:
            print(f"An error occurred for chunk {chunk_index + 1}: {e}")

        time.sleep(3)

# Запуск функции для получения данных и сохранения в Excel
fetch_data_for_qids(qid_name_map, "country_data_complete.xlsx")
