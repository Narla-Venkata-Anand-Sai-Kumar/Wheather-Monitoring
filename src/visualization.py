import sqlite3
import matplotlib.pyplot as plt

DB_FILE = 'weather.db'

def plot_daily_summary(city):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('SELECT dt, temp FROM weather WHERE city = ?', (city,))
    data = c.fetchall()
    dates = [row[0] for row in data]
    temps = [row[1] for row in data]
    
    plt.plot(dates, temps, label='Temperature')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title(f"Temperature Trend for {city}")
    plt.legend()
    plt.show()
    conn.close()
