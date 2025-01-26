import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the BBC Weather page for Berat, Albania
URL = "https://www.bbc.com/weather/3183875"

def scrape_weather():
    try:
        # Send a GET request to the BBC Weather page
        response = requests.get(URL)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # **1. Current Weather**
        current_temp = soup.find("span", class_="wr-value--temperature--c")
        current_condition = soup.find("div", class_="wr-day__weather-type-description")

        # Use default values if elements are missing
        current_temp = current_temp.get_text(strip=True) if current_temp else "N/A"
        current_condition = current_condition.get_text(strip=True) if current_condition else "N/A"

        # **2. Additional Details**
        details = soup.find_all("div", class_="wr-u-font-weight-500")
        wind_speed = details[0].get_text(strip=True) if len(details) > 0 else "N/A"
        humidity = details[1].get_text(strip=True) if len(details) > 1 else "N/A"
        visibility = details[2].get_text(strip=True) if len(details) > 2 else "N/A"
        uv_index = details[3].get_text(strip=True) if len(details) > 3 else "N/A"

        # **3. Hourly Forecast**
        hourly_forecast = []
        hourly_section = soup.find("div", class_="wr-time-slot-list")
        if hourly_section:
            for slot in hourly_section.find_all("li", class_="wr-time-slot"):
                time = slot.find("div", class_="wr-time-slot-primary__time")
                temp = slot.find("span", class_="wr-value--temperature--c")
                condition = slot.find("div", class_="wr-time-slot-primary__weather-type-description")

                # Use default values if elements are missing
                time = time.get_text(strip=True) if time else "N/A"
                temp = temp.get_text(strip=True) if temp else "N/A"
                condition = condition.get_text(strip=True) if condition else "N/A"
                hourly_forecast.append({"Time": time, "Temperature": temp, "Condition": condition})

        # **4. Daily Forecast**
        daily_forecast = []
        daily_section = soup.find("div", class_="wr-day-carousel")
        if daily_section:
            for day in daily_section.find_all("div", class_="wr-day"):
                date = day.find("h2", class_="wr-date")
                max_temp = day.find("span", class_="wr-value--temperature--c")
                summary = day.find("div", class_="wr-day__weather-type-description")

                # Use default values if elements are missing
                date = date.get_text(strip=True) if date else "N/A"
                max_temp = max_temp.get_text(strip=True) if max_temp else "N/A"
                summary = summary.get_text(strip=True) if summary else "N/A"
                daily_forecast.append({"Date": date, "Max Temperature": max_temp, "Summary": summary})

        # Save the data to CSV files
        # Current Weather
        current_weather = {
            "Temperature": current_temp,
            "Condition": current_condition,
            "Wind Speed": wind_speed,
            "Humidity": humidity,
            "Visibility": visibility,
            "UV Index": uv_index
        }
        pd.DataFrame([current_weather]).to_csv("current_weather.csv", index=False)

        # Hourly Forecast
        if hourly_forecast:
            pd.DataFrame(hourly_forecast).to_csv("hourly_forecast.csv", index=False)

        # Daily Forecast
        if daily_forecast:
            pd.DataFrame(daily_forecast).to_csv("daily_forecast.csv", index=False)

        print("Weather data scraped successfully:")
        print("- Current weather saved to current_weather.csv")
        print("- Hourly forecast saved to hourly_forecast.csv")
        print("- Daily forecast saved to daily_forecast.csv")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the webpage: {e}")
    except AttributeError as e:
        print(f"Error parsing the webpage: {e}")

# Run the function
if __name__ == "__main__":
    scrape_weather()
