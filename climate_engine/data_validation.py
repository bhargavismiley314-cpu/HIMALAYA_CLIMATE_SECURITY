def validate_weather_data(data):

    required_fields = [
        "temperature_2m",
        "relative_humidity_2m",
        "precipitation",
        "wind_speed_10m"
    ]

    if not isinstance(data, dict):
        return False

    for field in required_fields:
        if field not in data:
            return False

        value = data[field]

        if value is None:
            return False

        if isinstance(value, bool) or not isinstance(value, (int, float)):
            return False

    temperature = data["temperature_2m"]
    humidity = data["relative_humidity_2m"]
    precipitation = data["precipitation"]
    wind_speed = data["wind_speed_10m"]

    if not -90 <= temperature <= 60:
        return False

    if not 0 <= humidity <= 100:
        return False

    if precipitation < 0:
        return False

    if wind_speed < 0:
        return False

    return True
