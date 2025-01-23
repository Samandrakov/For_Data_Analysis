from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd
import math
import os

# Чтение CSV файла и извлечение QID и имен
df = pd.read_excel('qids_refactored.xlsx')
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
        SELECT ?company ?companyLabel ?numberOfEmployees ?headquartersLocation ?headquartersLocationLabel ?revenue ?revenueYear ?foundingDate ?officialWebsite ?dissolutionDate ?netProfit ?marketCapitalization ?totalAssets WHERE {{
          VALUES ?company {{ {values} }}  # Пример компаний

          OPTIONAL {{
            SELECT ?company (MAX(?emp) AS ?numberOfEmployees) WHERE {{
              ?company wdt:P1128 ?emp.
            }} GROUP BY ?company
          }}

          OPTIONAL {{
            SELECT ?company (SAMPLE(?location) AS ?headquartersLocation) WHERE {{
              ?company wdt:P159 ?location.
            }} GROUP BY ?company
          }}

          OPTIONAL {{
            SELECT ?company (SAMPLE(?rev) AS ?revenue) (SAMPLE(?revYear) AS ?revenueYear) WHERE {{
              ?company p:P2139 ?revenueStatement.
              ?revenueStatement ps:P2139 ?rev.
              ?revenueStatement pq:P585 ?revYear.
            }} GROUP BY ?company
          }}

          OPTIONAL {{
            SELECT ?company (MAX(?foundDate) AS ?foundingDate) WHERE {{
              ?company wdt:P571 ?foundDate.
            }} GROUP BY ?company
          }}

          OPTIONAL {{
            SELECT ?company (SAMPLE(?website) AS ?officialWebsite) WHERE {{
              ?company wdt:P856 ?website.
            }} GROUP BY ?company
          }}

          OPTIONAL {{
            SELECT ?company (MAX(?dissDate) AS ?dissolutionDate) WHERE {{
              ?company wdt:P576 ?dissDate.
            }} GROUP BY ?company
          }}

          OPTIONAL {{
            SELECT ?company (SAMPLE(?netProf) AS ?netProfit) WHERE {{
              ?company wdt:P2295 ?netProf.
            }} GROUP BY ?company
          }}

          OPTIONAL {{
            SELECT ?company (SAMPLE(?marketCap) AS ?marketCapitalization) WHERE {{
              ?company wdt:P2226 ?marketCap.
            }} GROUP BY ?company
          }}

          OPTIONAL {{
            SELECT ?company (SAMPLE(?assets) AS ?totalAssets) WHERE {{
              ?company wdt:P2403 ?assets.
            }} GROUP BY ?company
          }}

          SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }}
        }}
        """

        sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)

        try:
            results = sparql.query().convert()

            data = []
            for result in results["results"]["bindings"]:
                company = result.get("companyLabel", {}).get("value", "N/A")
                revenue = result.get("revenue", {}).get("value", "N/A")
                foundingDate = result.get("foundingDate", {}).get("value", "N/A")
                marketCapitalization = result.get("marketCapitalization", {}).get("value", "N/A")
                country = result.get("country", {}).get("value", "N/A")
                numberOfEmployees = result.get("numberOfEmployees", {}).get("value", "N/A")
                headquartersLocation = result.get("headquartersLocationLabel", {}).get("value", "N/A")
                officialWebsite = result.get("officialWebsite", {}).get("value", "N/A")
                dissolutionDate = result.get("dissolutionDate", {}).get("value", "N/A")

                for qid in chunk_qids:
                    data.append({
                        "QID": qid,
                        "Name": qid_name_map[qid],  # Добавляем имя из карты
                        "Company": company,
                        "Number of Employees": numberOfEmployees,
                        "Headquarters Location": headquartersLocation,
                        "Revenue": revenue,
                        "Founding Date": foundingDate,
                        "Official Website": officialWebsite,
                        "Dissolution Date": dissolutionDate,
                        "Market Capitalization": marketCapitalization,
                        "Country": country
                    })

            save_to_excel(data, filename, sheet_name='Sheet1')
            print(f"Data for chunk {chunk_index + 1}/{total_chunks} appended to {filename}")

        except Exception as e:
            print(f"An error occurred for chunk {chunk_index + 1}: {e}")

# Запуск функции для получения данных и сохранения в Excel
fetch_data_for_qids(qid_name_map, "company_data_complete_4.xlsx")
