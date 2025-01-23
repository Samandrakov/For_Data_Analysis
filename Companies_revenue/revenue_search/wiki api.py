import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def get_wikipedia_url(company):
    wiki_url = "https://en.wikipedia.org/wiki/"
    company_url = wiki_url + company
    # print(company_url)
    return company_url
def get_revenue_from_wikipedia(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    info_box = soup.find('table', {'class': 'infobox'})
    if not info_box:
        try:
            # print("Couldn't find company by Vanilla")
            response = requests.get(url+"_(company)")
            soup = BeautifulSoup(response.text, 'html.parser')
            info_box = soup.find('table', {'class': 'infobox'})
            if not info_box:
                return "Info box not found"
            else:
                pass
        except Exception as e:
            # print('Error in completing search url')
            return "Info box not found"

    rows = info_box.find_all('tr')

    for row in rows:
        header = row.find('th')
        if header and 'Revenue' in header.text:
            revenue = row.find('td').text.strip()
            return revenue
    return "Revenue not found"


def process_batch(batch_df):
    output_data = []
    output_file = 'output.csv'
    for index, row in batch_df.iterrows():

        name = row['name']

        url = get_wikipedia_url(name)
        revenue = get_revenue_from_wikipedia(url)
        # if revenue:
            # print(f'Revenue: {revenue}')
        # else:
            # print(f"Couldn't get revenue")
        output_data.append({
            'name': name,
            'revenue': revenue,

        })

    batch_output_df = pd.DataFrame(output_data)

    with open(output_file, 'a', newline='', encoding='utf-8') as f:
        batch_output_df.to_csv(f, header=f.tell() == 0, index=False)




def main():
    batch_size = 1
    input_file = 'names.xlsx'
    df = pd.read_excel(input_file)

    total_batches = (len(df) + batch_size - 1) // batch_size
    n = 0
    j = 0
    for i in range(total_batches):
        n += 1
        if n == 50:
            j +=1
            print(f"{n*j}/{total_batches}")
            n = 0
        start_idx = i * batch_size
        end_idx = start_idx + batch_size
        batch_df = df[start_idx:end_idx]

        # print(f"Processing batch {i + 1}/{total_batches}...")
        process_batch(batch_df)

        # time.sleep(0)

    print("Processing complete.")

if __name__ == "__main__":
    main()
