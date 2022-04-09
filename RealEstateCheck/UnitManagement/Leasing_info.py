import requests
json = {
	"leasing_info": {
		"leasing_type" 			       : "asdf",
		"is_sub_leasing_allowed"       : True,
		"application_fee"              : 123.23,
		"security_deposit"		       : 2313.32,
		"monthly_rent_1month_lease"    : None,
		"monthly_rent_6month_lease"    : None,
		"monthly_rent_12month_lease"   : None,
		"is_lease_termination_allowed" : False,
		"lease_termination_cost"  	   : 1232.23,
		"additional_leasing_clauses"   : "aditional info here...."
	}
}

response = requests.post("http://localhost:8000/unitmanagement/leasing_info/", json=json)

print(response.content)
# print(type(response.content))
print(response.status_code)
