from climate_engine.extreme_weather import detect_extreme_weather


def test_extreme_heat():
    weather = {
        "temperature_2m": 42,
        "wind_speed_10m": 20,
        "precipitation": 10
    }

    result = detect_extreme_weather(weather)

    assert result["status"] == "success"
    assert "Extreme Heat Warning" in result["alerts"]


def test_normal_weather():
    weather = {
        "temperature_2m": 25,
        "wind_speed_10m": 15,
        "precipitation": 5
    }

    result = detect_extreme_weather(weather)

    assert result["extreme_weather_detected"] is False


def test_invalid_weather():
    result = detect_extreme_weather(None)

    assert result["status"] == "error"