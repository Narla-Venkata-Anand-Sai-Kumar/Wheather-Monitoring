import sqlite3

DB_FILE = 'weather.db'

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS weather (
                 city TEXT, temp REAL, feels_like REAL, dt INTEGER)''')
    c.execute('''CREATE TABLE IF NOT EXISTS daily_summary (
                 city TEXT, avg_temp REAL, max_temp REAL, min_temp REAL, date TEXT)''')
    conn.commit()
    conn.close()

def store_weather_data(city, temp, feels_like, dt):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('INSERT INTO weather (city, temp, feels_like, dt) VALUES (?, ?, ?, ?)',
              (city, temp, feels_like, dt))
    conn.commit()
    conn.close()
