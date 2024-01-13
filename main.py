from flask import Flask, request
from utils import WeatherAPI

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def get_weather():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    return WeatherAPI.get_current_weather(lat, lon)

@app.route('/forecast', methods=['GET'])
def get_forecast():
    city = request.args.get('city')
    country = request.args.get('country')
    days = request.args.get('days')
    return WeatherAPI.get_weather_forecast(city, country, days)

@app.route('/atmospheric-pressure', methods=['GET'])
def get_atmospheric_pressure():
    city = request.args.get('city')
    country = request.args.get('country')
    return WeatherAPI.get_atmospheric_pressure(city, country)

if __name__ == '__main__':
    app.run(debug=True)