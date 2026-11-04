from climate_engine.avalanche import detect_avalanche_risk


def test_high_avalanche_risk():
    data = {
        "snowfall_24h_cm": 40,
        "wind_speed_kmh": 40,
        "slope_angle": 35
    }

    result = detect_avalanche_risk(data)

    assert result["status"] == "success"
    assert result["avalanche_risk_detected"] is True


def test_moderate_avalanche_risk():
    data = {
        "snowfall_24h_cm": 20,
        "wind_speed_kmh": 25,
        "slope_angle": 35
    }

    result = detect_avalanche_risk(data)

    assert "Moderate Avalanche Risk" in result["alerts"]


def test_normal_snowfall():
    data = {
        "snowfall_24h_cm": 5,
        "wind_speed_kmh": 10,
        "slope_angle": 15
    }

    result = detect_avalanche_risk(data)

    assert result["avalanche_risk_detected"] is False


def test_missing_data():
    data = {
        "snowfall_24h_cm": 30
    }

    result = detect_avalanche_risk(data)

    assert result["status"] == "error"


def test_invalid_data():
    result = detect_avalanche_risk("invalid")

    assert result["status"] == "error"