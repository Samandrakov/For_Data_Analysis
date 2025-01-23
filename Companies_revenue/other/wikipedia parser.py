import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus


def get_wikipedia_url(company_name):
    """Получите URL страницы Википедии для компании"""
    search_query = quote_plus(company_name + " Wikipedia")
    search_url = f'https://en.wikipedia.org/w/index.php?search={search_query}'

    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Попробуем найти первую ссылку на страницу Википедии
    results = soup.find_all('div', {'class': 'mw-search-result-heading'})
    if results:
        for result in results:
            link = result.find('a')
            if link:
                return 'https://en.wikipedia.org' + link['href']
    return None


def get_revenue_from_wikipedia(url):
    """Получите выручку с страницы Википедии"""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Найдите таблицу инфобокса
    info_box = soup.find('table', {'class': 'infobox'})
    if not info_box:
        return "Info box not found"

    rows = info_box.find_all('tr')

    # Извлеките выручку
    for row in rows:
        header = row.find('th')
        if header and 'Revenue' in header.text:
            revenue = row.find('td').text.strip()
            return revenue
    return "Revenue not found"


def main():

    company_name = 'Microsoft'
    print(f"Processing {company_name}...")
    wikipedia_url = get_wikipedia_url(company_name)
    if wikipedia_url:
        print(f"Found Wikipedia URL: {wikipedia_url}")
        revenue = get_revenue_from_wikipedia(wikipedia_url)
        print(f"Revenue for {company_name}: {revenue}")
    else:
        print(f"Could not find Wikipedia page for {company_name}")



if __name__ == "__main__":
    main()
