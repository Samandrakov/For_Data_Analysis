import requests
from bs4 import BeautifulSoup


def get_wikipedia_page(url):
    """Функция для получения содержимого страницы."""
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')


def get_university_info(university_name):
    """Получение информации о вузе и его координатах."""
    base_url = 'https://ru.wikipedia.org/wiki/'
    search_url = base_url + university_name.replace(' ', '_')

    soup = get_wikipedia_page(search_url)

    # Проверка наличия кнопки для перехода на английский
    en_link_element = soup.select_one("#p-lang > div > ul > li.interlanguage-link.interwiki-en.mw-list-item > a")

    if en_link_element:
        en_url = "https://ru.wikipedia.org" + en_link_element['href']
        soup = get_wikipedia_page(en_url)
    else:
        print(f"No English page found for {university_name}, using Russian page.")

    # Парсинг текстового описания
    description = soup.find('p').text.strip()

    # Парсинг координат
    coordinates = None
    geo_tag = soup.find('span', {'class': 'geo-dec'})
    if geo_tag:
        coordinates = geo_tag.text.strip()
    else:
        print(f"No coordinates found for {university_name}")

    return {
        "university": university_name,
        "description": description,
        "coordinates": coordinates
    }


def main():
    universities = ["МГУ", "СПбГУ", "Казанский федеральный университет"]

    for university in universities:
        info = get_university_info(university)
        print(f"University: {info['university']}")
        print(f"Description: {info['description']}")
        print(f"Coordinates: {info['coordinates']}")
        print("\n" + "-" * 50 + "\n")


if __name__ == "__main__":
    main()
