def calculate_overall_risk(risk_results):
    if not isinstance(risk_results, dict):
        return {
            "status": "error",
            "alerts": ["Invalid risk data"]
        }

    risk_keys = [
        "extreme_weather_detected",
        "flood_risk_detected",
        "glacier_melt_risk_detected",
        "glof_risk_detected",
        "landslide_risk_detected",
        "avalanche_risk_detected"
    ]

    alerts = []

    for key in risk_keys:
        if risk_results.get(key) is True:
            alerts.append(key.replace("_", " ").title())

    total_risks = len(alerts)

    if total_risks >= 4:
        overall_level = "Critical"
    elif total_risks >= 2:
        overall_level = "High"
    elif total_risks == 1:
        overall_level = "Moderate"
    else:
        overall_level = "Low"

    return {
        "status": "success",
        "overall_risk_level": overall_level,
        "total_risks_detected": total_risks,
        "alerts": alerts
    }