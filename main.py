import requests
from tkinter import *
from tkinter import ttk
from config import API_KEY,BASE_URL
from weather_ui import create_weather_ui

def get_weather(location):
    params = {
        'q': location,
        'appid': API_KEY,
        'units': 'imperial'
    }

    response = requests.get(BASE_URL, params)

    if response.status_code == 200:
        weather_data = response.json()
        temperature_label.config(text=f"Temperature: {weather_data['main']['temp']}°F")
        weather_description_label.config(text=f"Condition: {weather_data['weather'][0]['description']}")
        humidity_label.config(text=f"Humidity: {weather_data['main']['humidity']}%")

    elif response.status_code == 404:
        temperature_label.config(text="Error: not a valid city.")
        weather_description_label.config(text="")
        humidity_label.config(text="")
    else:
        temperature_label.config(text="Error: fetching weather data.")

def on_location_entry(event):
    location = location_entry.get()
    get_weather(location)

root = Tk()
root.title("Weather App")

location_entry, temperature_label, weather_description_label, humidity_label = create_weather_ui(root, on_location_entry, get_weather)

root.mainloop()