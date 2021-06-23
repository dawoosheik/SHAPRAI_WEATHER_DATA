import requests
from datetime import datetime

api_key = '7a29ec31ff7e0a26b5bfc895ed073cd9'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print("-------------------------------------------------------------------")
print("Weather Stats for - {}  ||  {}".format(location.upper(),date_time))
print("-------------------------------------------------------------------")

print("Current Temperature is   : {:.2f} deg C ".format(temp_city))
print("Current Weather Desc     :", weather_desc)
print("Current Humidity         :",hmdt,"%")
print("Current Wind speed       :",wind_spd,'kmph')
