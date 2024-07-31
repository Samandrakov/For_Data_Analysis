from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd
import math
import os
from list import values_list

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

def fetch_data_for_qids(qid_list, filename):
    # Разбиваем список на части по 50 QID
    chunk_size = 1
    total_chunks = math.ceil(len(qid_list) / chunk_size)

    for chunk_index in range(total_chunks):
        start = chunk_index * chunk_size
        end = start + chunk_size
        chunk_qids = qid_list[start:end]

        # Формируем строку QID для SPARQL запроса
        values = ' '.join(f'wd:{qid}' for qid in chunk_qids)
        query = f"""
        SELECT ?company ?companyLabel ?numberOfEmployees ?headquartersLocation ?headquartersLocationLabel ?revenue ?foundingDate ?officialWebsite ?dissolutionDate ?netProfit ?marketCapitalization ?totalAssets WHERE {{
          VALUES ?company {{ {values} }}  # Динамическая подстановка значений QID

          OPTIONAL {{ ?company wdt:P1128 ?numberOfEmployees. }}
          OPTIONAL {{ ?company wdt:P159 ?headquartersLocation. }}
          OPTIONAL {{ ?company wdt:P2139 ?revenue. }}
          OPTIONAL {{ ?company wdt:P571 ?foundingDate. }}
          OPTIONAL {{ ?company wdt:P856 ?officialWebsite. }}
          OPTIONAL {{ ?company wdt:P576 ?dissolutionDate. }}
          OPTIONAL {{ ?company wdt:P2295 ?netProfit. }}
          OPTIONAL {{ ?company wdt:P2226 ?marketCapitalization. }}
          OPTIONAL {{ ?company wdt:P2403 ?totalAssets. }}

          SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }}
        }}
        """

        # Инициализация SPARQLWrapper с указанием URL-адреса SPARQL-эндпоинта Wikidata
        sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)

        try:
            # Выполнение запроса и получение результатов
            results = sparql.query().convert()

            # Обработка результатов и накопление данных
            data = []
            for result in results["results"]["bindings"]:
                company = result.get("companyLabel", {}).get("value", "N/A")
                numberOfEmployees = result.get("numberOfEmployees", {}).get("value", "N/A")
                headquartersLocation = result.get("headquartersLocationLabel", {}).get("value", "N/A")
                # revenue = result.get("revenue", {}).get("value", "N/A")
                foundingDate = result.get("foundingDate", {}).get("value", "N/A")
                officialWebsite = result.get("officialWebsite", {}).get("value", "N/A")
                # dissolutionDate = result.get("dissolutionDate", {}).get("value", "N/A")
                # netProfit = result.get("netProfit", {}).get("value", "N/A")
                # marketCapitalization = result.get("marketCapitalization", {}).get("value", "N/A")
                totalAssets = result.get("totalAssets", {}).get("value", "N/A")

                # Добавляем номер QID в данные
                for qid in chunk_qids:
                    data.append({
                        "QID": qid,
                        "Company": company,
                        "Number of Employees": numberOfEmployees,
                        "Headquarters Location": headquartersLocation,
                        # "Revenue": revenue,
                        "Founding Date": foundingDate,
                        "Official Website": officialWebsite,
                        # "Dissolution Date": dissolutionDate,
                        # "Net Profit": netProfit,
                        # "Market Capitalization": marketCapitalization,
                        "Total Assets": totalAssets
                    })

            # Сохранение накопленных данных в Excel
            save_to_excel(data, filename, sheet_name='Sheet1')
            print(f"Data for chunk {chunk_index + 1}/{total_chunks} appended to {filename}")

        except Exception as e:
            print(f"An error occurred for chunk {chunk_index + 1}: {e}")

# Пример списка QID (замените на свой список QID)
# qid_list = ["Q1234", "Q5678", "Q91011", "Q121314", "Q151617", "Q181920"]  # Замените на ваши QID без "wd:"

# Запуск функции для получения данных и сохранения в Excel
fetch_data_for_qids(values_list, "company_data_complete_4.xlsx")
