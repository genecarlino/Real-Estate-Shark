import requests
json = {
	"unit": {
		"unit_type_id" 	 			 	: None,
		"community_id" 	 				: None,
		"address_id" 		 		 	: None,
		"leasing_info_id"  			 	: None,
		"num_of_bedrooms"  			 	: 1,
		"num_of_bathrooms" 			 	: 144,
		"num_of_balcony"			 	: 232,
		"is_available" 				 	: True,
		"is_reserved" 				 	: True,
		"unit_availability_start_date"  : None,
		"unit_availability_end_date"    : None,
		"unit_description" 			 	: None,
		"living_area_sf" 				: 1232,
		"unit_number" 				 	: None,
		"unit_at_floor" 				: None
	}
}
#
# Single Unit Get:
# response = requests.post("http://localhost:8000/unitmanagement/unit/", json=json)
# response = requests.get('http://localhost:8000/unitmanagement/unit/2/')
# print(response.content)
# print(response.status_code)

# Unit Listing
response = requests.get('http://localhost:8000/unitmanagement/unitlisting/')
print(response.content)
print(response.status_code)


