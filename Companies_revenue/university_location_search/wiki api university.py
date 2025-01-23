import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from get_en_version import get_location_from_wikipedia as glfw
from get_coordinates import get_coordinates_from_wikipedia as gcfw

def get_wikipedia_url(object_of_interest):
    wiki_url = "https://ru.wikipedia.org/wiki/"
    modified_url = wiki_url + object_of_interest.replace(' ', '_')
    # print(modified_url)
    return modified_url
#
#
# def get_additional_info_from_wikipedia(modified_url):
#     response = requests.get(modified_url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     # Найдите таблицу инфобокса
#     info_box = soup.find('table', {'class': 'infobox'})
#     if not info_box:
#         try:
#             print("Couldn't find vanilla object")
#
#             if not info_box:
#                 return "Info box not found"
#             else:
#                 pass
#         except Exception as e:
#             print('Error in completing search url')
#             return "Info box not found"
#
#     rows = info_box.find_all('tr')
#
#     # Извлеките характеристику
#     for row in rows:
#         header = row.find('th')
#         if header and 'Расположение' in header.text:
#             characterisitcs = row.find('td').text.strip()
#             return characterisitcs
#     return "characterisitcs not found"

def process_batch(batch_df):
    # Создание списка для хранения результатов
    output_data = []
    output_file = 'output.csv'
    for index, row in batch_df.iterrows():

        name = row['name']

        # Получение выручки и валюты
        url = get_wikipedia_url(name)
        characterisitcs = glfw(url)
        coodrinates = gcfw(url)

        if characterisitcs:
            print(f'characterisitcs: {characterisitcs}')
        else:
            print(f"Couldn't get characterisitcs")


        if coodrinates:
            print(f"coordinates: {coodrinates}")
        else:
            print(f"Couldn't get coodrinates")
        # Добавление данных в список
        output_data.append({
            'name': name,
            'location': characterisitcs,
            'coordinates': coodrinates

        })

    # Преобразование списка в DataFrame
    batch_output_df = pd.DataFrame(output_data)

    # Сохранение в CSV файл (добавляем к существующему файлу)
    with open(output_file, 'a', newline='', encoding='utf-8') as f:
        batch_output_df.to_csv(f, header=f.tell() == 0, index=False)


def main():
    batch_size = 1  # Размер батча
    input_file = 'education_name.xlsx'
    df = pd.read_excel(input_file)

    # Обработка данных батчами
    total_batches = (len(df) + batch_size - 1) // batch_size
    n = 0
    j = 0
    for i in range(total_batches):
        n += 1
        if n == 50:
            j += 1
            print(f"{n * j}/{total_batches}")
            n = 0
        start_idx = i * batch_size
        end_idx = start_idx + batch_size
        batch_df = df[start_idx:end_idx]

        print(f"Processing batch {i + 1}/{total_batches}...")
        process_batch(batch_df)

        # Небольшая задержка для предотвращения перегрузки сервера Wikidata
        # time.sleep(0)

    print("Processing complete.")


if __name__ == "__main__":
    main()
