import sqlite3
from database import store_weather_data

DB_FILE = 'weather.db'

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def process_weather_data(city, weather_data):
    temp_kelvin = weather_data['main']['temp']
    feels_like_kelvin = weather_data['main']['feels_like']
    temp_celsius = kelvin_to_celsius(temp_kelvin)
    feels_like_celsius = kelvin_to_celsius(feels_like_kelvin)
    dt = weather_data['dt']
    store_weather_data(city, temp_celsius, feels_like_celsius, dt)

def generate_daily_summary(city):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('SELECT temp FROM weather WHERE city = ? AND dt >= strftime("%s", "now", "-1 day")', (city,))
    temps = [row[0] for row in c.fetchall()]
    
    if temps:
        avg_temp = sum(temps) / len(temps)
        max_temp = max(temps)
        min_temp = min(temps)
        summary = {
            'avg_temp': avg_temp,
            'max_temp': max_temp,
            'min_temp': min_temp
        }
        conn.close()
        return summary
    return {}