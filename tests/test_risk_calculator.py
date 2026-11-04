from climate_engine.risk_calculator import calculate_overall_risk


def test_low_risk():
    data = {
        "extreme_weather_detected": False,
        "flood_risk_detected": False,
        "glacier_melt_risk_detected": False,
        "glof_risk_detected": False,
        "landslide_risk_detected": False,
        "avalanche_risk_detected": False
    }

    result = calculate_overall_risk(data)

    assert result["overall_risk_level"] == "Low"


def test_moderate_risk():
    data = {"flood_risk_detected": True}

    result = calculate_overall_risk(data)

    assert result["overall_risk_level"] == "Moderate"


def test_high_risk():
    data = {
        "flood_risk_detected": True,
        "landslide_risk_detected": True
    }

    result = calculate_overall_risk(data)

    assert result["overall_risk_level"] == "High"


def test_critical_risk():
    data = {
        "flood_risk_detected": True,
        "landslide_risk_detected": True,
        "avalanche_risk_detected": True,
        "glof_risk_detected": True
    }

    result = calculate_overall_risk(data)

    assert result["overall_risk_level"] == "Critical"


def test_invalid_data():
    result = calculate_overall_risk("invalid")

    assert result["status"] == "error"