#!/usr/bin/env python

import requests

#Specify the city with longitude and latitude
longitude = 73.8567   #Pune longitude
latitude = 18.5204    #Pune latitude


#api_key = does not require for this Open-Meteo Api. It is free.

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"


response = requests.get(url)
data = response.json()


#print(data)
#by printing data, we get all weather data in JSON
#if we want specific data then print each field
#code below


if response.status_code == 200:
    current = data['current_weather']
    print(f"Temperature: {current['temperature']}°C")
    print(f"Windspeed: {current['windspeed']} km/h")
    print(f"Weather code: {current['weathercode']}")
else:
    print("Error fetching weather data")




