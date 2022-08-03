import requests
import json

maricopa_url = 'https://api.weather.gov/points/33.0581,-112.0475'
forcast_url = 'https://api.weather.gov/gridpoints/PSR/157,40/forecast/hourly'

weather_API = requests.get(forcast_url)
print(weather_API.status_code)

json = weather_API.json()

tempurature = json.get("periods")[0].get("temperature")
print(tempurature)