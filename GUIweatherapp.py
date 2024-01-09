import requests
from tkinter import *
from tkinter import ttk
from config import API_KEY, BASE_URL

def get_weather():
    params =  {
        'q' : f'{"Irvine"},{"California"}',
        'appid' : API_KEY,
        'units': 'imperial'
    }

    response = requests.get(BASE_URL,params)

    if response.status_code == 200:
            weather_data = response.json()
            temperature_label.config(text=f"Temperature: {weather_data['main']['temp']}°F")
    else:
            temperature_label.config(text="Error fetching weather data.")


#Instantiating TLC and window
root = Tk()
root.title("Weather App")
frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="Current Weather in Irvine California").grid(column=0,row=0)

temperature_label = ttk.Label(frm, text="", font=("Arial", 16))
temperature_label.grid(column=0,row=2)

ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=3)

get_weather()

root.mainloop()
