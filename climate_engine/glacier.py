def detect_glacier_risk(weather):
    alerts = []

    if not isinstance(weather, dict):
        return {
            "status": "error",
            "alerts": ["Invalid weather data"]
        }

    temperature = weather.get("temperature_2m")

    if temperature is None:
        return {
            "status": "error",
            "alerts": ["Temperature data missing"]
        }

    if temperature >= 5:
        alerts.append("High Glacier Melting Risk")

    elif temperature >= 2:
        alerts.append("Moderate Glacier Melting Risk")

    return {
        "status": "success",
        "alerts": alerts,
        "glacier_melt_risk_detected": len(alerts) > 0
    }