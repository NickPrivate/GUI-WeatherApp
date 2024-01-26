# Weather App - Project Overview

The Weather App is a personal project aimed at gaining practical experience in building applications that integrate external APIs and create a graphical user interface (GUI) using Tkinter. This application allows users to retrieve real-time weather information for a specific location by making requests to a weather API.

## Features

- **Weather Data**: Retrieve current weather data, including temperature, condition, and humidity, for any city or location.
- **User-Friendly Interface**: The application features an intuitive and user-friendly GUI built using Tkinter, making it accessible for users of all levels.
- **Error Handling**: Implement error handling to provide informative feedback to users in case of invalid city names or failed API requests.
- **Modular Design**: The project follows a modular design pattern, separating the UI components from the main application logic for improved maintainability and scalability.

## System Requirements

- **Python**: The project is written in Python, so you need to have Python installed on your system.
 You can download Python from the official website: [Python Downloads](https://www.python.org/downloads/).

- **API Key**: To run the Weather App, you'll need to obtain an API key from a weather data provider.
  You can obtain a free API key from providers like [OpenWeatherMap](https://openweathermap.org/api).

- **External Libraries**: The project uses the following external libraries, which can be installed using pip:
  - ```pip install requests```
  - ```pip install tk```
 (usually included with Python)

# How to Run the Weather App
1. git clone https://github.com/NickPrivate/Weather-App.git
2. Navigate to the project directory:  
   ```cd Weather-App```

4. Create a **config.py** file with API_KEY and BASE_URL, Replace API_KEY with your API Key
```
  API_KEY = "YOUR API KEY HERE"
  BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
```
4. Run the Python script to start the Weather App  
   ```python main.py```
5. Enter the name of any City in the world and the program should display
   - Temperature (in Fahrenheit)
   - Condition
   - Humidity (percentage)

## Contributing
Contributions to this project are welcome. Feel free to submit bug reports, feature requests, or enhancements through GitHub Issues.
If you'd like to contribute code, please fork the repository, create a new branch for your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
