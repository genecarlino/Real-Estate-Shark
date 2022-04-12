import requests
response = requests.get("http://localhost:8000/unitmanagement/addresslisting/?offset=2&limit=100")
print(response.content)
print(response.status_code)
print(response.headers)