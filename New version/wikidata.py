from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd
import math
import os
import time

# Чтение CSV файла и извлечение QID и имен
df = pd.read_excel('names_qid.xlsx')
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
    # qid_list = []
    chunk_size = 1  # Измените размер чанка на необходимое значение
    total_chunks = math.ceil(len(qid_list) / chunk_size)

    for chunk_index in range(total_chunks):
        start = chunk_index * chunk_size
        end = start + chunk_size
        chunk_qids = qid_list[start:end]

        values = ' '.join(f'wd:{qid}' for qid in chunk_qids)
        query = f"""
        
                SELECT ?person ?personLabel ?birth_date ?birth_dateLabel ?place_of_birth ?place_of_birthLabel ?death_date ?death_dateLabel ?education ?educationLabel ?profession ?professionLabel ?party ?partyLabel WHERE {{
          VALUES ?person {{{values}}}
        
          OPTIONAL {{ ?person wdt:P569 ?birth_date. }}
          OPTIONAL {{ ?person wdt:P19 ?place_of_birth. }}
          OPTIONAL {{ ?person wdt:P570 ?death_date. }}
          OPTIONAL {{ ?person wdt:P69 ?education. }}
          OPTIONAL {{ ?person wdt:P106 ?profession. }}
          OPTIONAL {{ ?person wdt:P102 ?party. }}
        
          # Получаем метки для всех элементов
          SERVICE wikibase:label {{ 
            bd:serviceParam wikibase:language "[AUTO_LANGUAGE],ru".
            bd:serviceParam wikibase:label "ru".  # Указываем язык меток
          }}
        }}
        ORDER BY DESC(?birth_date)  # Сортировка по дате рождения
        LIMIT 1
        

        """

        sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)

        try:
            results = sparql.query().convert()
            print("Query executed successfully.")
            print("Query:", query)  # Отладочная информация: проверка запроса

            data = []
            if results["results"]["bindings"]:
                for result in results["results"]["bindings"]:
                    # Собираем данные с использованием метода get, чтобы обработать отсутствие полей
                    birth_date = result.get("birth_dateLabel", {}).get("value", "N/A")
                    place_of_birth = result.get("place_of_birthLabel", {}).get("value", "N/A")
                    death_date = result.get("death_dateLabel", {}).get("value", "N/A")
                    education = result.get("educationLabel", {}).get("value", "N/A")
                    profession = result.get("professionLabel", {}).get("value", "N/A")
                    party = result.get("partyLabel", {}).get("value", "N/A")


                    for qid in chunk_qids:
                        data.append({
                            "QID": qid,
                            "Name": qid_name_map[qid],  # Добавляем имя из карты
                            "birth_date": birth_date,
                            "place_of_birth": place_of_birth,
                            "death_date": death_date,
                            "education": education,
                            "profession": profession,
                            "party": party

                        })
            else:
                # Если результатов нет, добавляем только QID и имя
                for qid in chunk_qids:
                    data.append({
                        "QID": qid,
                        "Name": qid_name_map[qid],
                        "capital": "N/A",
                        "population": "N/A",
                        "officialLanguage": "N/A",
                        "governmentForm": "N/A",
                        "gdp": "N/A",
                        "inception": "N/A",
                        "Country": "N/A"
                    })

            save_to_excel(data, filename, sheet_name='Sheet1')
            print(f"Data for chunk {chunk_index + 1}/{total_chunks} appended to {filename}")
            print(data)
        except Exception as e:
            print(f"An error occurred for chunk {chunk_index + 1}: {e}")

        time.sleep(1)

# Запуск функции для получения данных и сохранения в Excel
fetch_data_for_qids(qid_name_map, "company_data_complete_1.xlsx")


