from climate_engine.glacier import detect_glacier_risk


def test_high_glacier_risk():
    weather = {"temperature_2m": 6}

    result = detect_glacier_risk(weather)

    assert result["status"] == "success"
    assert result["glacier_melt_risk_detected"] is True


def test_moderate_glacier_risk():
    weather = {"temperature_2m": 3}

    result = detect_glacier_risk(weather)

    assert "Moderate Glacier Melting Risk" in result["alerts"]


def test_normal_temperature():
    weather = {"temperature_2m": 0}

    result = detect_glacier_risk(weather)

    assert result["glacier_melt_risk_detected"] is False


def test_missing_temperature():
    weather = {}

    result = detect_glacier_risk(weather)

    assert result["status"] == "error"


def test_invalid_weather():
    result = detect_glacier_risk(None)

    assert result["status"] == "error"