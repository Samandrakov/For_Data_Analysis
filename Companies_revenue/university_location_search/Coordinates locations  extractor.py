import requests


def get_location(opencage_key, lat, lon):
    url = f"https://api.opencagedata.com/geocode/v1/json?q={lat}+{lon}&key={opencage_key}"

    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return None

    data = response.json()

    if data['status']['code'] != 200:
        print(f"Error: {data['status']['message']}")
        return None

    address = data['results'][0]['formatted']
    return address


if __name__ == "__main__":
    opencage_key = '14f0db8d1ffa4821b908f603292a94e0'

    latitude = 37.7749
    longitude = -122.4194

    location = get_location(opencage_key, latitude, longitude)

    if location:
        print(f"Address: {location}")
    else:
        print("Unable to get location.")
