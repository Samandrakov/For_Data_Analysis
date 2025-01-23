import requests
from bs4 import BeautifulSoup

def get_coordinates_from_wikipedia(url):
    if 'https://en.' in url:
        print('en website')
        geo_selector = 'span.geo-dec'
    elif 'https://ru.' in url:
        print('ru website')
        geo_selector = '#mw-indicator-0-coord > div > span > span > a'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    geo_info = soup.select_one(geo_selector)
    if geo_info:
        return geo_info.text
    else:
        print(f"Coordinates not found\nRedirecting to eng version")
        link_element = soup.select_one('#p-lang > div > ul > li.interlanguage-link.interwiki-en.mw-list-item > a')

        if link_element:
            # Извлечь URL из атрибута href
            href = link_element['href']
            response = requests.get(href)
            soup = BeautifulSoup(response.text, 'html.parser')
            geo_selector = 'span.geo-dec'
            geo_info = soup.select_one(geo_selector)
            if geo_info:
                return geo_info.text
            else:
                return 'Coord extraction error'

