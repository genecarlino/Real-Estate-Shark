from ast import Add
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import (Leasing_Info_Serializer, Address_Serializer, Unit_Type_Serializer,
Community_Serializer, Unit_Serializer)
from .models import Address
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict
from django.http import HttpResponse

class Unit_View(APIView):
    pass

class Community_View(APIView):
    pass

class Unit_Type_View(APIView):
    pass

class Leasing_Info_View(APIView):
    pass

class AddressList(APIView):
    def get(self, request):
        parameters = request.GET
        if ('offset' in parameters and 'limit' in parameters 
            and parameters['offset'].isnumeric() and parameters['limit'].isnumeric()):
            offset = int(parameters['offset'])
            limit = int(parameters['limit'])
            limit = offset + limit
            addresses = [{
                "id"                : address.id,
                "street_address" 	: address.street_address,o
			    "city"			    : address.city,
			    "state" 	 		: address.state,
				"county"  		    : address.county,
				"zip"  			    : address.zip
                } for address in Address.objects.all()[offset:limit]
            ]
            print(len( Address.objects.all()[offset:limit]))

            finalJson  = {
                "AddressObject" : {
                    "addresses" : addresses,
                    "count"     :  Address.objects.all().count()
                }
            }
            return Response(finalJson)
        else:
            return Response("404", status=status.HTTP_404_NOT_FOUND)



class Address_View(APIView):
    def get(self, request, id):
        # address will check if objects with said parameters exist
        address = Address.objects.filter(id=id)
        if Address.objects.filter(id=id).exists():
            address = Address.objects.get(id=id)
            data = model_to_dict(address)
            return Response(data)
        else:
            return Response("404", status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, id):
        if 'address' in request.data and Address.objects.filter(id=id).exists():
            address = Address.objects.get(id=id)
            serializer = Address_Serializer(address ,data=request.data['address'], partial=True)
            if serializer.is_valid():
                print("is valid")
                serializer.save()
                return Response('valid data')
            else:
                return Response("Invalid data", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Invalid data", status=status.HTTP_400_BAD_REQUEST)



class Post_Leasing_Info_View(APIView):
    def post(self, request):
        if "leasing_info" in request.data:
            leasingSerializer = Leasing_Info_Serializer(data=request.data["leasing_info"])
            if leasingSerializer.is_valid():
                leasingSerializer.save()
                print("serializer valid")
                return Response("valid data", status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response("Invalid data", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Invalid data", status=status.HTTP_400_BAD_REQUEST)

class Post_Address_View(APIView):
    # def get(self, request):
    #     nums = request.GET
    #     return Response(nums)
    # --------------------------
    # Get DONT USE BELOW!!
    # response = requests.get("http://localhost:8000/unitmanagement/address/?id=2")
    # print(response.content)
    # print(response.status_code)
    #----------------------------

    def post(self, request):
        if 'address' in request.data:
            serializer = Address_Serializer(data=request.data['address'])
            if serializer.is_valid():
                print("is valid")
                serializer.save()
                return Response('valid data')
            else:
                return Response("Invalid data", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Invalid data", status=status.HTTP_400_BAD_REQUEST)


class Post_Unit_Type_View(APIView):
    def post(self, request):
        if 'unit_type' in request.data:
            serializer = Unit_Type_Serializer(data=request.data['unit_type'])
            if serializer.is_valid():
                print("is valid")
                serializer.save()
                return Response('valid data')
            else:
                return Response("Invalid data", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Invalid data", status=status.HTTP_400_BAD_REQUEST)


class Post_Community_View(APIView):
    def post(self, request):
        if "community" in request.data:
            serializer = Community_Serializer(data=request.data["community"])
            if serializer.is_valid():
                print("is valid")
                serializer.save()
                return Response('valid data')
            else:
                return Response("Invalid data", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Invalid data", status=status.HTTP_400_BAD_REQUEST)

class Post_Unit_View(APIView):
    def post(self, request):
        if "unit" in request.data:
            serializer = Unit_Serializer(data=request.data["unit"])
            if serializer.is_valid():
                print("is valid")
                serializer.save()
                return Response('valid data')
            else:
                return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Invalid data", status=status.HTTP_400_BAD_REQUEST)
