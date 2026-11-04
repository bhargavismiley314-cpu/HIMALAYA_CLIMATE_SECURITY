from climate_engine.glof import detect_glof_risk


def test_critical_glof_risk():
    lake_data = {
        "water_level": 95,
        "dam_stability": 20
    }

    result = detect_glof_risk(lake_data)

    assert result["status"] == "success"
    assert result["glof_risk_detected"] is True


def test_moderate_glof_risk():
    lake_data = {
        "water_level": 80,
        "dam_stability": 70
    }

    result = detect_glof_risk(lake_data)

    assert "Moderate GLOF Risk" in result["alerts"]


def test_normal_lake():
    lake_data = {
        "water_level": 40,
        "dam_stability": 90
    }

    result = detect_glof_risk(lake_data)

    assert result["glof_risk_detected"] is False


def test_missing_lake_data():
    result = detect_glof_risk({})

    assert result["status"] == "error"


def test_invalid_lake_data():
    result = detect_glof_risk(None)

    assert result["status"] == "error"