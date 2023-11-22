from flask import Flask, render_template
import random
import time

app = Flask(__name__)

class WeatherStation:
    def __init__(self):
        self.data = []

    def collect_data(self):
        # Simulated data collection
        temperature = round(random.uniform(10, 35), 2)
        humidity = round(random.uniform(20, 80), 2)
        pressure = round(random.uniform(980, 1050), 2)
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        self.data.append({
            "timestamp": timestamp,
            "temperature (°C)": temperature,
            "humidity (%)": humidity,
            "pressure (hPa)": pressure,
        })

    def analyze_data(self):
        if not self.data:
            return None

        avg_temperature = sum(entry["temperature (°C)"] for entry in self.data) / len(self.data)
        avg_humidity = sum(entry["humidity (%)"] for entry in self.data) / len(self.data)
        avg_pressure = sum(entry["pressure (hPa)"] for entry in self.data) / len(self.data)

        return {
            "avg_temperature": avg_temperature,
            "avg_humidity": avg_humidity,
            "avg_pressure": avg_pressure,
        }

weather_station = WeatherStation()

@app.route('/')
def index():
    weather_station.collect_data()
    analysis_result = weather_station.analyze_data()
    return render_template('index.html', data=weather_station.data, analysis_result=analysis_result)

if __name__ == '__main__':
    app.run(debug=True)
