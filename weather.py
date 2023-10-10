import requests

API_KEY = "8e6d06f0a15d0b645114a9eaf33c9e45"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
#we need to install module which allows sending request to api: pip install requests

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print("Weather:", weather)
    temperature = round(data["main"]["temp"] - 273.15, 2)
    print("Temperature", temperature, "celcius")
else:
    print("An error occured")