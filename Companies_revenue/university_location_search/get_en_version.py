import requests
from bs4 import BeautifulSoup

# # url = 'https://ru.wikipedia.org/wiki/%D0%90%D0%B1%D0%B5%D1%80%D0%B4%D0%B8%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D1%83%D0%BD%D0%B8%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%82%D0%B5%D1%82'
# url = 'https://ru.wikipedia.org/wiki/%D0%A3%D0%BD%D0%B8%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%82%D0%B5%D1%82_%D0%94%D0%B0%D0%BC%D0%B0%D1%81%D0%BA%D0%B0'
def get_location_from_wikipedia(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    info_box = soup.find('table', {'class': 'infobox'})
    try:
        rows = info_box.find_all('tr')
    except Exception as e:
        pass
    if info_box:
        characterisitcs = 0
        for row in rows:
            header = row.find('th')
            if header and 'Расположение' in header.text:
                characterisitcs = row.find('td').text.strip()
            else:
                pass
        if characterisitcs != 0:
            print(f'Characteristics = {characterisitcs}')
            return characterisitcs
        elif characterisitcs == 0:
            print("Couldn't find characteristics in Russian")
            # Найти элемент ссылки по указанному селектору
            link_element = soup.select_one('#p-lang > div > ul > li.interlanguage-link.interwiki-en.mw-list-item > a')

            if link_element:
                # Извлечь URL из атрибута href
                href = link_element['href']
                response = requests.get(href)
                soup = BeautifulSoup(response.text, 'html.parser')
                info_box = soup.find('table', {'class': 'infobox'})
                rows = info_box.find_all('tr')
                if info_box:
                    characterisitcs = 0
                    for row in rows:
                        header = row.find('th')
                        if header and 'Location' in header.text:
                            try:
                                characterisitcs = row.find('td').text.strip()
                            except Exception as e:
                                pass
                        else:
                            pass
            if characterisitcs != 0:
                return characterisitcs
            else:
                print('no info')
                return




