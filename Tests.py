# test_weather_station.py

import pytest
from your_weather_station_module import WeatherStation

@pytest.fixture
def setup_weather_station():
    return WeatherStation()

# Test Case ID: TC001
def test_correct_data_received(setup_weather_station):
    # Known weather conditions
    known_data = {
        "temperature": 25.0,
        "windspeed": 10.0,
        "wind_direction": "N",
        "air_pressure": 1010.0,
        "rainfall": 0.0,
    }

    # Simulate collecting data in the Weather Station
    setup_weather_station.collect_data(known_data["temperature"], known_data["windspeed"],
                                       known_data["wind_direction"], known_data["air_pressure"],
                                       known_data["rainfall"])

    # Retrieve collected data from the Weather Station
    observed_data = setup_weather_station.get_collected_data()

    # Compare observed data with known data
    for key, value in known_data.items():
        assert value - 1 <= observed_data[key] <= value + 1

# Test Case ID: TC002
def test_correct_weather_conditions_reported(setup_weather_station):
    # Known weather conditions
    known_data = {
        "temperature": 25.0,
        "windspeed": 10.0,
        "wind_direction": "N",
        "air_pressure": 1010.0,
        "rainfall": 0.0,
    }

    # Simulate collecting data in the Weather Station
    setup_weather_station.collect_data(known_data["temperature"], known_data["windspeed"],
                                       known_data["wind_direction"], known_data["air_pressure"],
                                       known_data["rainfall"])

    # Retrieve analyzed data from the Weather Station
    analyzed_data = setup_weather_station.analyze_data()

    # Compare analyzed data with known data
    for key, value in known_data.items():
        assert value - 1 <= analyzed_data[key] <= value + 1

# Test Case ID: TC003
def test_correct_status_information_sent(setup_weather_station):
    # Known status mode
    known_status = "NORMAL"

    # Set the status mode in the Weather Station
    setup_weather_station.set_status_mode(known_status)

    # Retrieve status information sent to the weather information system
    observed_status = setup_weather_station.send_status_information()

    # Compare observed status with known status
    assert observed_status == known_status

# Test Case ID: TC004
def test_maximum_load_conditions_performance(setup_weather_station):
    # Known maximum load conditions
    known_max_conditions = {
        "temperature": 35.0,
        "windspeed": 20.0,
        "wind_direction": "S",
        "air_pressure": 1050.0,
        "rainfall": 5.0,
        "runtime_speed": 100,
    }

    # Overload the Weather Station to simulate peak usage
    for _ in range(100):  # Simulate multiple data collections for peak usage
        setup_weather_station.collect_data(known_max_conditions["temperature"],
                                           known_max_conditions["windspeed"],
                                           known_max_conditions["wind_direction"],
                                           known_max_conditions["air_pressure"],
                                           known_max_conditions["rainfall"])

    # Retrieve analyzed data from the Weather Station
    analyzed_data = setup_weather_station.analyze_data()

    # Retrieve runtime speed of the Weather Station
    runtime_speed = setup_weather_station.get_runtime_speed()

    # Compare analyzed data with known data
    for key, value in known_max_conditions.items():
        assert value - 1 <= analyzed_data[key] <= value + 1

    # Compare runtime speed with defined maximum performance
    assert runtime_speed <= 100 + 5  # Assuming maximum defined speed is 100
