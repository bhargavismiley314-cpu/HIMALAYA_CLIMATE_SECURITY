def detect_extreme_weather(weather):
    alerts = []

    if not isinstance(weather, dict):
        return {
            "status": "error",
            "alerts": ["Invalid weather data"]
        }

    temperature = weather.get("temperature_2m")
    wind_speed = weather.get("wind_speed_10m")
    precipitation = weather.get("precipitation")

    if temperature is not None and temperature >= 40:
        alerts.append("Extreme Heat Warning")

    if wind_speed is not None and wind_speed >= 60:
        alerts.append("High Wind Warning")

    if precipitation is not None and precipitation >= 50:
        alerts.append("Heavy Rainfall Warning")

    return {
        "status": "success",
        "alerts": alerts,
        "extreme_weather_detected": len(alerts) > 0
    }