def detect_glof_risk(lake_data):
    alerts = []

    if not isinstance(lake_data, dict):
        return {
            "status": "error",
            "alerts": ["Invalid lake data"]
        }

    water_level = lake_data.get("water_level")
    dam_stability = lake_data.get("dam_stability")

    if water_level is None or dam_stability is None:
        return {
            "status": "error",
            "alerts": ["Missing lake information"]
        }

    if water_level >= 90 and dam_stability <= 30:
        alerts.append("Critical GLOF Risk")

    elif water_level >= 75 or dam_stability <= 50:
        alerts.append("Moderate GLOF Risk")

    return {
        "status": "success",
        "alerts": alerts,
        "glof_risk_detected": len(alerts) > 0
    }