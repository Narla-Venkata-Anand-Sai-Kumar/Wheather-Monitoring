from flask import Flask, render_template, request , redirect, url_for
from weather_api import get_weather_data
from processing import generate_daily_summary
from alerts import check_alerts
import sqlite3

app = Flask(__name__)

CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]

# Route for the home page
@app.route('/')
def home():
    summaries = []
    for city in CITIES:
        # Get today's weather summary
        summary = generate_daily_summary(city)
        summaries.append({
            'city': city,
            'summary': summary
        })
    return render_template('index.html', summaries=summaries)

# Route for alert threshold (optional)
@app.route('/alerts', methods=['POST'])
def set_alert_threshold():
    city = request.form.get('city')
    threshold = request.form.get('threshold')
    
    # Add your logic for handling the alert (e.g., store it or process it)
    print(f"Alert set for {city} with threshold {threshold}°C")

    # Ensure you return a valid response
    return redirect(url_for('home'))  # Re

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
