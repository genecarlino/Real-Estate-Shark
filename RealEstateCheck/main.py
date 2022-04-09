import requests
content = {
	"address": {
		"street_address": "4996 Jadewood Farms",
		"city": "Baltimore",
		"state": "Maryland",
		"county": "Baltimore",
		"zip": "21201"
	}
}

# response = requests.post("http://localhost:8000/unitmanagement/address/Jason=sugar,1,2,3,4", json=content)
response = requests.get("http://localhost:8000/unitmanagement/")

print(response.content)
print(type(response.content))
print(response.status_code)
