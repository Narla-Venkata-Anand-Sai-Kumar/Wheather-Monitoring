from weather_api import get_weather_data
from processing import process_weather_data, generate_daily_summary
from alerts import check_alerts
from visualization import plot_daily_summary
import time

CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]

def main():
    while True:
        for city in CITIES:
            weather_data = get_weather_data(city)
            if weather_data:
                process_weather_data(city, weather_data)
                generate_daily_summary(city)
                check_alerts(city)
        time.sleep(300)  # 5-minute interval

if __name__ == "__main__":
    main()
