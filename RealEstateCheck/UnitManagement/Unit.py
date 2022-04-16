import requests

unit  = {
	"unit": {
		"community": {
				"street_address" 	: "12 superman road",
				"city" 			 	:  "Bolivard",
				"state" 			: "New York",
				"county" 			: "Williams",
				"zip" 				: "343434",
				"community_name"  	: "City group",
			},
		"leasing_info" :{
			"leasing_type" 				 	: "Group 1",
			"is_sub_leasing_allowed"  		: True,
			"application_fee"  			 	: 120.12,
			"security_deposit" 			 	: 132.02,
			"monthly_rent_1month_lease" 	: 132.02,
			"monthly_rent_6month_lease" 	: 132.02,
			"monthly_rent_12month_lease" 	: 132.02,
			"is_lease_termination_allowed"  : True,
			"lease_termination_cost" 		: 132.02,
			"additional_leasing_clauses" 	: "Data given to lease people",
		},
			"unit_type" 					 	: "condo",
			"street_address" 				: "12 superman road",
			"city" 						 	: "New York",
			"state" 						: "New York",
			"county" 						: "Williams",
			"zip" 						 	: "12345",
			"num_of_bedrooms"  			 	: 12,
			"num_of_bathrooms" 			 	: 213,
			"num_of_balcony"	 			: 2,
			"is_available"     			 	: True,
			"is_reserved" 	 			 	: False,
			"unit_availability_start_date"  : '2022-04-09',
			"unit_availability_end_date"    : '2022-04-12',
			"unit_description" 			 	: "Valid unit super good",
			"living_area_sf" 				: 1600,
			"unit_number" 					: 12,
			"unit_at_floor" 				: 0,

		}

}
#
# Single Unit Get:
# response = requests.post("http://localhost:8000/unitmanagement/unit/", json=json)
response = requests.get('http://localhost:8000/unitmanagement/unit/2/')
print(response.content)
print(response.status_code)

response = requests.get('http://localhost:8000/unitmanagement/unitlisting/')
print(response.content)
print(response.status_code)

#Unit Listing
# for x in range(100):
# 	response = requests.post('http://localhost:8000/unitmanagement/unit/', json=unit)
# 	print(response.content)
# 	print(response.status_code)


