### README.md

markdown
# Weather Monitoring Web Application

## Project Overview

This web application monitors real-time weather conditions for various metro cities in India using the OpenWeatherMap API. The application fetches weather data, processes it to provide daily summaries (including average, max, min temperatures), and allows users to set temperature thresholds for alerts. The app has a beautiful UI powered by Bootstrap and displays daily weather summaries with icons representing different weather conditions.

## Features

- Fetches real-time weather data from OpenWeatherMap API for cities: Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad.
- Converts temperature from Kelvin to Celsius.
- Provides daily weather summaries including:
  - Average temperature
  - Maximum temperature
  - Minimum temperature
  - Dominant weather condition
- Set user-configurable temperature thresholds for alerting.
- Uses Bootstrap for a responsive and modern UI.
- Stores daily weather summaries in an SQLite database.
- Flask-based backend and a clear, interactive frontend.

## Bonus Features
- Extendable to support additional weather parameters (humidity, wind speed, etc.).
- Can be expanded to handle weather forecast summaries from OpenWeatherMap.
- Includes user-configurable threshold alerting for weather conditions.

## Prerequisites

Before setting up the project, ensure you have the following installed:

- Python 3.7+
- Flask 2.0+
- An OpenWeatherMap API key ([sign up here](https://openweathermap.org/api) to get a free API key)

## Installation

1. **Clone the repository**:
    bash
    git clone https://github.com/your-username/weather-monitoring.git
    cd weather-monitoring
    

2. **Create a virtual environment** (recommended):
    bash
    python3 -m venv venv
    source venv/bin/activate
    

3. **Install the dependencies**:
    bash
    pip install -r requirements.txt
    

4. **Set up the database**:
    Initialize the SQLite database by running the following command:
    bash
    python3 -c "from database import init_db; init_db()"
    

5. **Add your OpenWeatherMap API key**:
    Add key in the src/weather_api.py file
    OpenWeatherMap API key:
    
    OPENWEATHER_API_KEY=your_api_key_here
    

6. **Run the application**:
    Start the Flask development server by running:
    bash
    python3 app.py
    

7. **Access the application**:
    Open your browser and go to:
    
    http://127.0.0.1:5000
    

## Usage

- The main page displays daily weather summaries for metro cities.
- You can set an alert threshold by selecting a city and a temperature value. If the temperature exceeds the threshold in real-time updates, an alert will be triggered.

## Testing

- To test the alert system, try setting a threshold and simulate API calls by running `weather.py` manually with updated data.
- Test weather updates by manually fetching weather data using the `weather.py` script.

## Additional Notes

- The application currently uses SQLite for persistent storage, but you can easily swap it for a more robust database (e.g., PostgreSQL, MySQL) by updating the SQLAlchemy configuration.
- If you're running the app in production, ensure to set up proper security layers (e.g., SSL, environment variable management) as well as performance optimizations like caching.
  
## Dependencies

- Flask: For serving the web application.
- SQLAlchemy: For database ORM.
- Requests: To call the OpenWeatherMap API.
- Bootstrap 5: For responsive UI design.

To install all dependencies:
bash
pip install -r requirements.txt

## License

This project is licensed under the MIT License.

---

## Contact

For any queries or issues, feel free to reach out:

- Author: Narla Venkata Anand Sai Kuma
- Email: venkatnarla0@gmail.com
