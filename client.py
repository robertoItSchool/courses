import requests

url = 'http://localhost:8000/hello'
response = requests.get(url)

print(response)
print(response.content)
