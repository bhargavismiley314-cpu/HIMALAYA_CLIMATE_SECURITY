
import json
from urllib.request import urlopen
from urllib.parse import urlencode
from urllib.error import URLError, HTTPError


def collect_weather_data(latitude, longitude):

    parameters = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m",
        "timezone": "auto"
    }

    url = (
        "https://api.open-meteo.com/v1/forecast?"
        + urlencode(parameters)
    )

    try:
        with urlopen(url, timeout=15) as response:
            data = json.loads(
                response.read().decode("utf-8")
            )

        return {
            "status": "success",
            "location": {
                "latitude": latitude,
                "longitude": longitude
            },
            "weather": data.get("current", {})
        }

    except (HTTPError, URLError, TimeoutError) as error:
        return {
            "status": "error",
            "message": str(error)
        }
