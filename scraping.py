import pandas as pd
import os
from Crypto.Random import get_random_bytes  # For generating a random encryption key
import encryption  # Import the encryption module
from api_integration import fetch_current_weather, fetch_forecast  # Import functions

def save_weather_data(city_name):
    # Fetch data from the API
    current_weather = fetch_current_weather(city_name)
    hourly_forecast, daily_forecast = fetch_forecast(city_name)

    if not current_weather or not hourly_forecast or not daily_forecast:
        print("Failed to fetch data from WeatherAPI.")
        return

    try:
        # **1. Save Current Weather**
        pd.DataFrame([current_weather]).to_csv("current_weather.csv", index=False)

        # **2. Save Hourly Forecast**
        pd.DataFrame(hourly_forecast).to_csv("hourly_forecast.csv", index=False)

        # **3. Save Daily Forecast**
        pd.DataFrame(daily_forecast).to_csv("daily_forecast.csv", index=False)

        print("Weather data saved successfully:")
        print("- Current weather saved to current_weather.csv")
        print("- Hourly forecast saved to hourly_forecast.csv")
        print("- Daily forecast saved to daily_forecast.csv")
    except KeyError as e:
        print(f"Error processing weather data: Missing key {e}")

if __name__ == "__main__":
    city_name = "Vlora"  # Replace with any city name if needed

    # Save weather data to CSV files
    save_weather_data(city_name)

    # Encrypt the current_weather.csv file
    encryption_key = get_random_bytes(16)  # Generate a random AES key
    input_file = "current_weather.csv"
    encrypted_file = "current_weather_encrypted.bin"

    if os.path.exists(input_file):
        encryption.encrypt_file(input_file, encrypted_file, encryption_key)
        print(f"File '{input_file}' encrypted successfully to '{encrypted_file}'")
        print(f"Encryption completed. Key: {encryption_key.hex()}")
