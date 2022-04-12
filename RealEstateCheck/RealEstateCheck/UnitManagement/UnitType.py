import requests
json = {
	"unit_type": {
		"unit_type": "bandana"
	}
}

response = requests.post("http://localhost:8000/unitmanagement/unit_type/", json=json)
print(response.content)
# print(type(response.content))
print(response.status_code)
