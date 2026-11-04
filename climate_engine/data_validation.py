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

        if data[field] is None:
            return False

    return True