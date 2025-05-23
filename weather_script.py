import requests
import os

def fetch_weather(api_key, city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  
    }
    response = requests.get(url, params=params)
    return response.json()  # Always return the JSON response

if __name__ == "__main__":

    API_KEY = os.getenv("OPENWEATHER_API_KEY")  # Set your API key as an environment variable
    city = input("Enter city name: ")  # Change to your desired city

    if not API_KEY:
        print("Please set the OPENWEATHER_API_KEY environment variable.")
    else:
        try:
            weather = fetch_weather(API_KEY, city)
            if weather.get('cod') != 200:
                print(f"Error: {weather.get('message', 'Unknown error')}")
            else:
                print(f"Weather in {city}: {weather['weather'][0]['description']}, Temperature: {weather['main']['temp']}°C")
        except Exception as e:
            print(f"Error fetching weather data: {e}")