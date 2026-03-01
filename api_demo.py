import requests

lat = 10.00
lon = 20.00
url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m"

response = requests.get(url)

##print(response)

data = response.json()

## print(data)

temprature = data["current"]["temperature_2m"]

print(f"Temperature is: {temprature}°C")
