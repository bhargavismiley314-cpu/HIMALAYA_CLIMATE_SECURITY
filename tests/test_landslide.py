from climate_engine.landslide import detect_landslide_risk


def test_high_landslide_risk():
    data = {
        "rainfall_mm": 120,
        "soil_moisture": 90,
        "slope_angle": 40
    }

    result = detect_landslide_risk(data)

    assert result["status"] == "success"
    assert result["landslide_risk_detected"] is True


def test_moderate_landslide_risk():
    data = {
        "rainfall_mm": 60,
        "soil_moisture": 70,
        "slope_angle": 25
    }

    result = detect_landslide_risk(data)

    assert "Moderate Landslide Risk" in result["alerts"]


def test_normal_weather():
    data = {
        "rainfall_mm": 10,
        "soil_moisture": 30,
        "slope_angle": 10
    }

    result = detect_landslide_risk(data)

    assert result["landslide_risk_detected"] is False


def test_missing_data():
    data = {
        "rainfall_mm": 100
    }

    result = detect_landslide_risk(data)

    assert result["status"] == "error"


def test_invalid_data():
    result = detect_landslide_risk("invalid")

    assert result["status"] == "error"