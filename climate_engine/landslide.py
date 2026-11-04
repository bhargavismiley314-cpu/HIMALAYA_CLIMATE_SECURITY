def detect_landslide_risk(landslide_data):

    alerts = []

    if not isinstance(landslide_data, dict):
        return {
            "status": "error",
            "alerts": ["Invalid landslide data"]
        }

    rainfall = landslide_data.get("rainfall_mm")
    soil_moisture = landslide_data.get("soil_moisture")
    slope_angle = landslide_data.get("slope_angle")

    if rainfall is None or soil_moisture is None or slope_angle is None:
        return {
            "status": "error",
            "alerts": ["Missing landslide information"]
        }

    if rainfall >= 100 and soil_moisture >= 80 and slope_angle >= 30:
        alerts.append("High Landslide Risk")

    elif rainfall >= 50 and soil_moisture >= 60 and slope_angle >= 20:
        alerts.append("Moderate Landslide Risk")

    return {
        "status": "success",
        "alerts": alerts,
        "landslide_risk_detected": len(alerts) > 0
    }