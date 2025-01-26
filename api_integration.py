import requests

# WeatherAPI details
API_KEY = "244a0faf2bff417bb81192506252601"
BASE_URL = "http://api.weatherapi.com/v1"

def fetch_current_weather(city_name):
    """
    Fetches current weather data from WeatherAPI for a given city.
    """
    try:
        url = f"{BASE_URL}/current.json"
        params = {"key": API_KEY, "q": city_name}
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        # Extract and return relevant details
        return {
            "City": city_name,
            "Temperature": data["current"]["temp_c"],
            "Condition": data["current"]["condition"]["text"],
            "Wind Speed": data["current"]["wind_kph"],
            "Humidity": data["current"]["humidity"],
            "Visibility": data["current"]["vis_km"],
            "UV Index": data["current"]["uv"],
        }
    except requests.exceptions.RequestException as e:
        print(f"Error fetching current weather data: {e}")
        return None

def fetch_forecast(city_name, days=3):
    """
    Fetches weather forecast data from WeatherAPI for a given city.
    """
    try:
        url = f"{BASE_URL}/forecast.json"
        params = {"key": API_KEY, "q": city_name, "days": days}
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        # Extract and return the forecast details
        hourly_forecast = []
        daily_forecast = []

        # Extract hourly forecast for the first day
        for hour in data["forecast"]["forecastday"][0]["hour"]:
            hourly_forecast.append({
                "Time": hour["time"],
                "Temperature": hour["temp_c"],
                "Condition": hour["condition"]["text"]
            })

        # Extract daily forecast
        for day in data["forecast"]["forecastday"]:
            daily_forecast.append({
                "Date": day["date"],
                "Max Temperature": day["day"]["maxtemp_c"],
                "Min Temperature": day["day"]["mintemp_c"],
                "Condition": day["day"]["condition"]["text"],
            })

        return hourly_forecast, daily_forecast
    except requests.exceptions.RequestException as e:
        print(f"Error fetching forecast data: {e}")
        return None, None

if __name__ == "__main__":
    # Example usage
    city = "Berat"
    print("Fetching current weather...")
    print(fetch_current_weather(city))

    print("Fetching forecast...")
    hourly, daily = fetch_forecast(city)
    print("Hourly Forecast:", hourly)
    print("Daily Forecast:", daily)
