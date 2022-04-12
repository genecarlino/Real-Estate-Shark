import requests
#Post
# json = {
# 	"address": {
# 		"street_address" 	: "213123",
# 		"city" 			    : "3f33rf",
# 		"state" 	 		: "3f33rf",
# 		"county"  		    : "3f33rf",
# 		"zip"  			    : "3f33rf",
# 	}
# }
# response = requests.post("http://localhost:8000/unitmanagement/address/", json=json)
# print(response.content)
# # print(type(response.content))
# print(response.status_code)
#Get
# response = requests.get("http://localhost:8000/unitmanagement/address/?id=2")
# print(response.content)
# print(response.status_code)

#Get
# response = requests.get("http://localhost:8000/unitmanagement/address/2/")
# print(response.content)
# print(response.status_code)

#Put
json = {
	"address": {
		"state" 	 		: "Nebraska",
	}
}
#
response = requests.get("http://localhost:8000/unitmanagement/address/2/")
print(response.content)
print(response.status_code)

response = requests.put("http://localhost:8000/unitmanagement/address/2/", json=json)
print(response.content)
print(response.status_code)

response = requests.get("http://localhost:8000/unitmanagement/address/2/")
print(response.content)
print(response.status_code)