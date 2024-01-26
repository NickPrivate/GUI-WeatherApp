from tkinter import *
from tkinter import ttk

def create_weather_ui(root, on_location_entry,get_weather):

    frm = ttk.Frame(root, padding=10)
    frm.grid()
    style = ttk.Style()
    style.theme_use('clam')


    ttk.Label(frm, text="Enter Location:").grid(column=0, row=0)
    location_entry = ttk.Entry(frm)
    location_entry.grid(column=1, row=0)
    location_entry.bind("<Return>", on_location_entry)

    ttk.Button(frm, text="Get Weather", command=lambda: get_weather(location_entry.get())).grid(column=2, row=0)

    temperature_label = ttk.Label(frm, text="", font=("Arial", 16))
    temperature_label.grid(column=0, row=2, columnspan=3)

    weather_description_label = ttk.Label(frm, text="")
    weather_description_label.grid(column=0, row=3, columnspan=3)

    humidity_label = ttk.Label(frm, text="")
    humidity_label.grid(column=0, row=4, columnspan=3)

    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=5)

    return location_entry, temperature_label, weather_description_label, humidity_label
