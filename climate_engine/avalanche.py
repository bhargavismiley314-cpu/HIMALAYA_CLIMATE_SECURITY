def detect_avalanche_risk(avalanche_data):

    alerts = []

    if not isinstance(avalanche_data, dict):
        return {
            "status": "error",
            "alerts": ["Invalid avalanche data"]
        }

    snowfall = avalanche_data.get("snowfall_24h_cm")
    wind_speed = avalanche_data.get("wind_speed_kmh")
    slope_angle = avalanche_data.get("slope_angle")

    if snowfall is None or wind_speed is None or slope_angle is None:
        return {
            "status": "error",
            "alerts": ["Missing avalanche information"]
        }

    if snowfall >= 30 and wind_speed >= 30 and 30 <= slope_angle <= 45:
        alerts.append("High Avalanche Risk")

    elif snowfall >= 15 and wind_speed >= 20 and 25 <= slope_angle <= 50:
        alerts.append("Moderate Avalanche Risk")

    return {
        "status": "success",
        "alerts": alerts,
        "avalanche_risk_detected": len(alerts) > 0
    }