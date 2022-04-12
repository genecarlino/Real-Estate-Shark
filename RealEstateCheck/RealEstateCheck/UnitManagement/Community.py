import requests
#Post
# json = {
# 	"community": {
# 		"community_name": "bandana"
# 	}
# }
#
# response = requests.post("http://localhost:8000/unitmanagement/community/", json=json)
# print(response.content)
# print(type(response.content))
# print(response.status_code)

#Put
json = {
	"community": {
		"community_name": "YO HO YO ho pirates life for me"
	}
}

response = requests.put("http://localhost:8000/unitmanagement/community/1/", json=json)
print(response.content)
print(response.status_code)