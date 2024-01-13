import requests

class WeatherAPI:
    BASE_URL = 'https://api.openweathermap.org/data/2.5'
    API_KEY = ''  # Replace with your OpenWeatherMap API key

    @staticmethod
    def get_current_weather(lat, lon):
        url = f'{WeatherAPI.BASE_URL}/weather?lat={lat}&lon={lon}&appid={WeatherAPI.API_KEY}'
        response = requests.get(url, timeout=5)
        data = response.json()
        return {'temperature': data['main']['temp'], 'weather': data['weather'][0]['description']}

    @staticmethod
    def get_weather_forecast(city, country, days):
        url = f'{WeatherAPI.BASE_URL}/forecast?q={city},{country}&cnt={days}&appid={WeatherAPI.API_KEY}'
        response = requests.get(url, timeout=5)
        data = response.json()
        return {'forecast': data['list']}

    @staticmethod
    def get_atmospheric_pressure(city, country):
        url = f'{WeatherAPI.BASE_URL}/weather?q={city},{country}&appid={WeatherAPI.API_KEY}'
        response = requests.get(url, timeout=5)
        data = response.json()
        return {'atmospheric_pressure': data['main']['pressure']}