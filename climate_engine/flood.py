def detect_flood_risk(weather):
    alerts = []

    if not isinstance(weather, dict):
        return {
            "status": "error",
            "alerts": ["Invalid weather data"]
        }

    precipitation = weather.get("precipitation")
    humidity = weather.get("relative_humidity_2m")

    if precipitation is not None and precipitation >= 50:
        alerts.append("Heavy Rainfall - Flood Risk")

    if humidity is not None and humidity >= 90:
        alerts.append("Very High Humidity Warning")

    return {
        "status": "success",
        "alerts": alerts,
        "flood_risk_detected": len(alerts) > 0
    }