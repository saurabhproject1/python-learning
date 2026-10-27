import requests

url = "https://en.wikipedia.org/wiki/Samosa"
response = requests.get(url)

print(response.text)