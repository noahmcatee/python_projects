# Work in progress.

#import datetime
import requests
import json

maricopa_url = 'https://api.weather.gov/points/33.0581,-112.0475'
forcast_url = 'https://api.weather.gov/gridpoints/PSR/157,40/forecast/hourly'

weather_API = requests.get(forcast_url)
if weather_API.status_code == 200:
    print("Website query successful. Status code", weather_API.status_code)

json = weather_API.json()
weather = json["properties"]["periods"]
# print(weather)
temperature = json["properties"]["periods"][0]["temperature"]
print("The temperature in Maricopa is", temperature)
forecast = json["properties"]["periods"][0]["shortForecast"]
print("The forcast is", forecast)
data_time = json["properties"]["periods"][0]["startTime"]
print("This data was queried for", data_time)

#tempurature = json.get("periods")[0].get("temperature")
#print(tempurature)
