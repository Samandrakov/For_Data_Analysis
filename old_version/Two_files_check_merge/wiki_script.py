import requests
import csv

# Initialize an empty list to store results
results_data = []

# Wikidata SPARQL endpoint
endpoint_url = "https://query.wikidata.org/sparql"

# Define the CSV file containing names
csv_file_name = "output.csv"

# Define the CSV fieldnames (column names) for reading names
csv_fieldnames = ["name"]

# Read names from the CSV file
with open(csv_file_name, mode="r", encoding="utf-8") as csv_file:
    reader = csv.DictReader(csv_file, fieldnames=csv_fieldnames)
    for row in reader:
        search_name = row["name"]

        # Your SPARQL query to retrieve person data
        query = f"""
        
            SELECT DISTINCT
                ?person ?personLabel ?birthDate ?placeOfBirthLabel ?sitelink_en ?sitelink_ru ?educationLabel ?ed_startTimeLabel ?ed_endTimeLabel
            WHERE {{
              SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],ru". }}

              ?person wdt:P31 wd:Q5;
                      wdt:P27 wd:Q217;
                      rdfs:label ?name.

              OPTIONAL {{
                ?person wdt:P569 ?birthDate.
              }}

              OPTIONAL {{
              ?sitelink_ru schema:about ?person;
              schema:isPartOf <https://ru.wikipedia.org/>.
              }}

              OPTIONAL {{
              ?sitelink_en schema:about ?person;
              schema:isPartOf <https://en.wikipedia.org/>.
              }}

              OPTIONAL {{
                ?person wdt:P19 ?placeOfBirth.
                ?placeOfBirth rdfs:label ?placeOfBirthLabel.
                FILTER(LANG(?placeOfBirthLabel) = "ru")
              }}

              OPTIONAL {{
                ?person p:P69 ?educationStatement.
                ?educationStatement ps:P69 ?education.
                ?education rdfs:label ?educationLabel.
                FILTER(LANG(?educationLabel) = "en")
                OPTIONAL {{
                  ?educationStatement pq:P580 ?ed_startTime.
                  BIND(YEAR(?ed_startTime) AS ?ed_startTimeLabel)
                }}
                OPTIONAL {{
                  ?educationStatement pq:P582 ?ed_endTime.
                  BIND(YEAR(?ed_endTime) AS ?ed_endTimeLabel)
                }}
              }}

              BIND("{search_name}" AS ?searchName)


              FILTER (
                CONTAINS(?name, ?searchName) ||
                CONTAINS(?name, ?givenName) && CONTAINS(?name, ?familyName)
              )
            }}
            LIMIT 5000
        """

        # Define the request headers
        headers = {
            "User-Agent": "MyWikidataRequest/1.0 (your@email.com)",
            "Accept": "application/sparql-results+json",
        }

        # Define the request parameters
        params = {
            "query": query,
            "format": "json",
        }

        # Send the SPARQL query request
        response = requests.get(endpoint_url, headers=headers, params=params)

        # Check if the response is successful
        if response.status_code == 200:
            data = response.json()
            if "results" in data and "bindings" in data["results"]:
                bindings = data["results"]["bindings"]
                for binding in bindings:
                    # Extract the person's Wikidata ID (QID)
                    person_id = binding["person"]["value"]
                    # Initialize a dictionary for the person's data
                    person_data = {}
                    person_data["person"] = person_id
                    for key, value in binding.items():
                        person_data[key] = value["value"]
                    # Add the link to the person's Wikidata entity
                    person_data["wikidataLink"] = f"http://www.wikidata.org/entity/{person_id.split('/')[-1]}"
                    # Append the person's data to the results list
                    results_data.append(person_data)

# Define the CSV file name for saving results
csv_file_name = "results.csv"

# Define the CSV fieldnames (column names) for saving results
csv_fieldnames = [
    "person",
    "personLabel",
    "birthDate",
    "placeOfBirthLabel",
    "sitelink_ru",
    "sitelink_en",
    "educationLabel",
    "ed_startTimeLabel",
    "ed_endTimeLabel",
    "wikidataLink",  # Add the column for the Wikidata entity link
]

# Process results to format as described
formatted_results = []
for person_data in results_data:
    formatted_person_data = {}
    formatted_person_data["person"] = person_data.get("personLabel", None)
    formatted_person_data["personLabel"] = person_data.get("personLabel", None)
    formatted_person_data["birthDate"] = person_data.get("birthDate", None)
    formatted_person_data["placeOfBirthLabel"] = person_data.get("placeOfBirthLabel", None)
    formatted_person_data["sitelink_ru"] = person_data.get("sitelink_ru", None)
    formatted_person_data["sitelink_en"] = person_data.get("sitelink_en", None)
    formatted_person_data["educationLabel"] = person_data.get("educationLabel", None)
    formatted_person_data["ed_startTimeLabel"] = person_data.get("ed_startTimeLabel", None)
    formatted_person_data["ed_endTimeLabel"] = person_data.get("ed_endTimeLabel", None)
    formatted_person_data["wikidataLink"] = person_data.get("wikidataLink", None)  # Include the link
    formatted_results.append(formatted_person_data)

# Write the results to the CSV file
with open(csv_file_name, mode="w", encoding="utf-8", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_fieldnames)
    writer.writeheader()
    for row in formatted_results:
        writer.writerow(row)

print(f"Results saved to {csv_file_name}")
