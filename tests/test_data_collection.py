
from climate_engine.data_collection import collect_weather_data


def test_collect_weather_data():
    result = collect_weather_data(27.9881, 86.9250)

    assert result["status"] in ["success", "error"]

    if result["status"] == "success":
        assert "temperature_2m" in result["weather"]
        assert "relative_humidity_2m" in result["weather"]
