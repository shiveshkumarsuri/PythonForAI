import requests

print("Hello, World!")
response = requests.get('https://api.github.com')
print(response.status_code)