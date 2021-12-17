# pip install requests
import requests

response = requests.get("https://api.openweathermap.org/data/2.5/forecast")

print(response.headers)
js = response.json()
print(js, type(js))
