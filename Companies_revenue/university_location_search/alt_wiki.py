import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


def extract_info_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            # The result is a Wikipedia URL
            response = requests.get(result)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract characteristics
            info_box = soup.find('table', {'class': 'infobox'})
            characteristics = "Info box not found"
            if info_box:
                rows = info_box.find_all('tr')
                for row in rows:
                    header = row.find('th')
                    if header and 'Расположение' in header.text:
                        characteristics = row.find('td').text.strip()
                        break

            # Extract coordinates
            coordinates = "Coordinates not found"
            geo = soup.find('span', {'class': 'geo'})
            if geo:
                coordinates = geo.text.strip()

            return characteristics, coordinates
        return result

    return wrapper


@extract_info_decorator
def get_wikipedia_url(object_of_interest):
    wiki_url = "https://ru.wikipedia.org/wiki/"
    modified_url = wiki_url + object_of_interest.replace(' ', '_')
    print(modified_url)
    return modified_url


@extract_info_decorator
def get_additional_info_from_wikipedia(modified_url):
    return modified_url


def process_batch(batch_df):
    # Создание списка для хранения результатов
    output_data = []
    output_file = 'output.csv'
    for index, row in batch_df.iterrows():

        name = row['name']

        # Получение характеристик и координат
        url = get_wikipedia_url(name)
        characteristics, coordinates = get_additional_info_from_wikipedia(url)

        if characteristics:
            print(f'Characteristics: {characteristics}')
        else:
            print("Couldn't get characteristics")

        if coordinates:
            print(f'Coordinates: {coordinates}')
        else:
            print("Couldn't get coordinates")

        # Добавление данных в список
        output_data.append({
            'name': name,
            'location': characteristics,
            'coordinates': coordinates
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
        time.sleep(1)

    print("Processing complete.")


if __name__ == "__main__":
    main()
