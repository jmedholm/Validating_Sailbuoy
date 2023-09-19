import requests
import urllib.parse

def get_latlon(location):
    url = 'https://nominatim.openstreetmap.org/search?q=' + urllib.parse.quote(location) + '&format=json'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error if the response status code is not successful
        response_data = response.json()
        
        if not response_data:
            print('Location not found:', location)
            return None
        
        lat = float(response_data[0]["lat"])
        lon = float(response_data[0]["lon"])
        
        return lat, lon
    
    except requests.exceptions.RequestException as e:
        print('An error occurred:', e)
        return None