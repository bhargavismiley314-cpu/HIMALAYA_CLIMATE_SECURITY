from climate_engine.data_validation import validate_weather_data


def test_valid_weather_data():
    data = {
        "temperature_2m": 25,
        "relative_humidity_2m": 60,
        "precipitation": 0,
        "wind_speed_10m": 10
    }

    assert validate_weather_data(data) is True


def test_missing_weather_data():
    data = {
        "temperature_2m": 25
    }

    assert validate_weather_data(data) is False
    def test_invalid_temperature():
    data = {
        "temperature_2m": 100,
        "relative_humidity_2m": 60,
        "precipitation": 0,
        "wind_speed_10m": 10
    }

    assert validate_weather_data(data) is False


def test_invalid_humidity():
    data = {
        "temperature_2m": 25,
        "relative_humidity_2m": 150,
        "precipitation": 0,
        "wind_speed_10m": 10
    }

    assert validate_weather_data(data) is False
    def test_invalid_precipitation():
    data = {
        "temperature_2m": 25,
        "relative_humidity_2m": 60,
        "precipitation": -5,
        "wind_speed_10m": 10
    }

    assert validate_weather_data(data) is False


def test_invalid_wind_speed():
    data = {
        "temperature_2m": 25,
        "relative_humidity_2m": 60,
        "precipitation": 0,
        "wind_speed_10m": -10
    }

    assert validate_weather_data(data) is False
