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
import requests

API_KEY = '179686ef4b7232b8d0f0417d08b5c487'  # Replace with your OpenWeatherMap API key
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        return weather
    else:
        print(f"Error: {response.status_code} - {response.json().get('message', '')}")
        return None

def display_weather(weather):
    if weather:
        print(f"Weather in {weather['city']}:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Description: {weather['description'].capitalize()}")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind Speed: {weather['wind_speed']} m/s")
    else:
        print("Could not retrieve weather data.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    weather = get_weather(city)
    display_weather(weather)