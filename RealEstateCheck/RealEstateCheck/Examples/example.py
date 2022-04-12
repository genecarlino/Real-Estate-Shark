import requests

response = requests.get("http://localhost:8000/unitmanagement/example/", )
print(response.content)
# print(type(response.content))
print(response.status_code)
