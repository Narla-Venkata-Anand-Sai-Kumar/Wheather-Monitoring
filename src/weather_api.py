import requests

API_KEY = "-insert here-"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

CITY_IDS = {
    "Delhi": 1273294,
    "Mumbai": 1275339,
    "Chennai": 1264527,
    "Bangalore": 1277333,
    "Kolkata": 1275004,
    "Hyderabad": 1269843
}

def get_weather_data(city):
    city_id = CITY_IDS.get(city)
    if not city_id:
        return None
    
    params = {
        "id": city_id,
        "appid": API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None
