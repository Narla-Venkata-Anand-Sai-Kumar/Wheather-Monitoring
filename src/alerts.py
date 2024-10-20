import sqlite3

DB_FILE = 'weather.db'

def check_alerts(city, threshold=35):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('SELECT temp FROM weather WHERE city = ? ORDER BY dt DESC LIMIT 2', (city,))
    recent_temps = [row[0] for row in c.fetchall()]
    
    if len(recent_temps) == 2 and all(temp > threshold for temp in recent_temps):
        print(f"ALERT! Temperature in {city} exceeded {threshold}°C")
    conn.close()
