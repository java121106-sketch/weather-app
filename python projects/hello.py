import requests
from config import api_key
cityname = input("enter a city name:")

url = f"https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={api_key}&units=metric"
response = requests.get(url).json()

temperature = response["main"]["temp"]
feelslike = response["main"]["feels_like"]
weather = response["weather"][0]["description"]
print("temperature:",temperature,"℃")
print("temperature feels like:",feelslike,"℃")
print("weather:",weather)