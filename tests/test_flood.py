from climate_engine.flood import detect_flood_risk


def test_high_rainfall():
    weather = {
        "precipitation": 80,
        "relative_humidity_2m": 95
    }

    result = detect_flood_risk(weather)

    assert result["status"] == "success"
    assert result["flood_risk_detected"] is True


def test_normal_weather():
    weather = {
        "precipitation": 5,
        "relative_humidity_2m": 50
    }

    result = detect_flood_risk(weather)

    assert result["flood_risk_detected"] is False


def test_invalid_weather():
    result = detect_flood_risk(None)

    assert result["status"] == "error"