import requests
import json

url = "https://community-open-weather-map.p.rapidapi.com/weather"

querystring = {"q":"Boston","lat":"0","lon":"0","callback":"test","id":"2172797","lang":"null","units":"imperial","mode":"xml"}

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "1b7c1d10f6msh0499dc592ca145dp1a8e44jsnd13bba6646f1"
    }

response = requests.get(url, headers=headers, params=querystring)
data = json.loads(response.text[5:-1])

print(f"Current temp is: {data['main']['temp']}")