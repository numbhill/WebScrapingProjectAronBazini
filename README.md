# Weather Data Fetching and Encryption Project

This project combines API integration, data processing, file encryption, and weather data forecasting. It fetches real-time weather data, stores the results in CSV files, and provides an option to encrypt sensitive weather information using AES encryption.

## Features

### 1. **Fetch Weather Data**
- Retrieves **current weather** and **forecast data** from the [WeatherAPI](https://www.weatherapi.com/).
- Retrieves both hourly and daily weather forecasts for a specified city.
- Data includes temperature, condition, wind speed, humidity, visibility, and more.
- Example functionality is provided in `api_integration.py`.

### 2. **Save Weather Data**
- Saves the fetched weather data to CSV files:
  - `current_weather.csv`
  - `hourly_forecast.csv`
  - `daily_forecast.csv`
- Each CSV file is systematically created using the **Pandas** library.
- The saving mechanism is implemented in `scraping.py`.

### 3. **Encrypt Weather Data**
- Encrypts the `current_weather.csv` file using **AES (Advanced Encryption Standard)**.
- Provides options to securely encrypt and decrypt files.
- Encryption and decryption functionalities are located in `encryption.py`.

## Project Structure

```plaintext
├── api_integration.py       # Fetches weather data from WeatherAPI
├── scraping.py              # Saves weather data and calls encryption methods
├── encryption.py            # AES encryption and decryption for files
├── current_weather.csv      # Sample CSV file with current weather data
├── hourly_forecast.csv      # Sample hourly forecast CSV
├── daily_forecast.csv       # Sample daily forecast CSV
├── current_weather_encrypted.bin  # AES-encrypted binary file
```

## Files Overview

1. **`api_integration.py`**  
   Handles API calls to fetch current weather and forecast data from WeatherAPI.  
   - **Functions**:
     - `fetch_current_weather(city_name)`: Fetches the current weather for a city.
     - `fetch_forecast(city_name, days=3)`: Retrieves an hourly and daily forecast for a city (default: 3 days).

2. **`scraping.py`**  
   Saves the weather data into CSV files, using `api_integration.py` for weather data and `encryption.py` for AES encryption.  
   - **Key Feature**:
     - Programmatically fetches and saves weather data for a city.
     - Encrypts the `current_weather.csv` data file and generates a binary output.

3. **`encryption.py`**  
   Handles encryption and decryption for sensitive weather data files using AES.  
   - **Functions**:
     - `encrypt_file(input_file, output_file, key)`: Encrypts the input file and saves it to the output file.
     - `decrypt_file(input_file, output_file, key)`: Decrypts an encrypted file and restores it to its original state.

4. **Sample Weather Data Files**:
   - `current_weather.csv`: Stores single-day weather data for the specified city.
   - `hourly_forecast.csv`: Shows hourly weather forecast data.
   - `daily_forecast.csv`: Provides a multi-day weather forecast summary.

5. **`current_weather_encrypted.bin`**  
   A sample AES-encrypted file demonstrating the encryption of weather data.

## Setup Requirements

To run this project locally, you’ll need the following:

### Prerequisites
1. Python 3.8+
2. Required libraries:
   - `requests`: For making API calls.
   - `pandas`: For handling CSV file manipulations.
   - `pycryptodome`: For AES encryption.

Install the required libraries using:
```bash
pip install requests pandas pycryptodome
```

### API Key
The project uses WeatherAPI to fetch weather data. You need to have an API key from [WeatherAPI](https://www.weatherapi.com/). Place your API key in `api_integration.py`:
```python
API_KEY = "YOUR_API_KEY_HERE"
```

## How to Run the Project

1. Ensure all dependencies are installed.
2. Replace the placeholder city name (e.g., `Vlora`) with the desired city.
3. Execute `scraping.py` to fetch, save, and encrypt weather data:
   ```bash
   python scraping.py
   ```
4. The script will:
   - Save the weather data in CSV files.
   - Encrypt `current_weather.csv` and save the encrypted output to `current_weather_encrypted.bin`.

5. To decrypt the file, use the same key that was generated during encryption:
   ```python
   encryption.decrypt_file(input_file, output_file, key)
   ```

## Example Workflow

1. Fetch the real-time weather data for `Vlora`.
2. Save the results to the following CSV files:
   - `current_weather.csv`
   - `hourly_forecast.csv`
   - `daily_forecast.csv`
3. Encrypt the `current_weather.csv` file and store the output in `current_weather_encrypted.bin`.

## Output File Examples

### `hourly_forecast.csv`
| Time              | Temperature | Condition       |
|-------------------|-------------|-----------------|
| 2025-01-26 00:00 | 11.6 °C     | Clear           |
| 2025-01-26 01:00 | 11.5 °C     | Clear           |
| 2025-01-26 02:00 | 11.7 °C     | Overcast        |

### `daily_forecast.csv`
| Date         | Max Temperature | Min Temperature | Condition       |
|--------------|-----------------|-----------------|-----------------|
| 2025-01-26   | 15.5 °C         | 11.4 °C         | Partly Cloudy   |
| 2025-01-27   | 15.5 °C         | 11.0 °C         | Sunny           |

