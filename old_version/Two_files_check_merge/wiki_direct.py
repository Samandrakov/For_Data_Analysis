from wikidata.client import Client
import openpyxl

# Initialize the Wikidata client
client = Client()

# List of country codes
country_codes = [
    "Q865"
]


# Function to get official languages, capital, GDP, and population for a country
def get_country_data(country_code):
    entity = client.get(country_code, load=True)

    # Official languages
    official_languages = entity.data.get('claims', {}).get('P37', [])
    languages = []
    for lang in official_languages:
        lang_entity_id = lang.get('mainsnak', {}).get('datavalue', {}).get('value', {}).get('id')
        if lang_entity_id:
            lang_entity = client.get(lang_entity_id, load=True)
            lang_name = lang_entity.data['labels'].get('ru', {}).get('value', 'Unknown')
            languages.append(lang_name)

    # Capital
    capital = entity.data.get('claims', {}).get('P36', [])
    capital_name = 'None'
    if capital:
        capital_entity_id = capital[0].get('mainsnak', {}).get('datavalue', {}).get('value', {}).get('id')
        if capital_entity_id:
            capital_entity = client.get(capital_entity_id, load=True)
            capital_name = capital_entity.data['labels'].get('ru', {}).get('value', 'Unknown')

    # GDP (nominal)
    gdp = entity.data.get('claims', {}).get('P2131', [])
    gdp_value = 'None'
    if gdp:
        gdp_amount = gdp[0].get('mainsnak', {}).get('datavalue', {}).get('value', {}).get('amount')
        if gdp_amount:
            gdp_value = float(gdp_amount)

    # Population
    population = entity.data.get('claims', {}).get('P1082', [])
    population_value = 'None'
    if population:
        population_amount = population[0].get('mainsnak', {}).get('datavalue', {}).get('value', {}).get('amount')
        if population_amount:
            population_value = int(population_amount)

    return {
        'languages': languages,
        'capital': capital_name,
        'gdp': gdp_value,
        'population': population_value
    }


# Create a dictionary to store the results
country_data = {}

# Fetch the official languages, capital, GDP, and population for each country
for code in country_codes:
    country_data[code] = get_country_data(code)

# Create a new Excel workbook and sheet
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Country Data"

# Write headers to the Excel sheet
headers = ["Country Code", "Official Languages", "Capital", "GDP (Nominal)", "Population"]
ws.append(headers)

# Write country data to the Excel sheet
for code, data in country_data.items():
    row = [
        code,
        ', '.join(data['languages']) if data['languages'] else 'None',
        data['capital'],
        data['gdp'],
        data['population']
    ]
    ws.append(row)

# Save the Excel workbook
wb.save("Country_Data.xlsx")

print("Data successfully written to Country_Data.xlsx")
