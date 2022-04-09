import requests

response = requests.get("http://localhost:8000/unitmanagement/addresslisting/?limit=2&offset=5")
print(response.content)
print(response.status_code)
print(response.headers)