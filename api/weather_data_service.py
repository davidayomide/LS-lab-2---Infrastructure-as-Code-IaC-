import requests

def get_weather_data(location, api_key):
    api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(location, api_key)
    response = requests.get(api_url)
    return response.json()

weather_data = get_weather_data("London", "7f3fa893d85a38a0a4d9b468bb423365")
print(weather_data)

