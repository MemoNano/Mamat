import requests
import pprint
import json

# url = "https://maps.googleapis.com/maps/api/geocode/json?address=595 Market Street San Francisco, " \
#       "CA 94105&key=AIzaSyC56ho80KnfUqsochlmCiVDYF_VVUayiXc"
#
# get_url = requests.get(url)
# get_google_json = get_url.json()
# pprint.pprint(get_google_json)
# elements = get_google_json["results"]
# print("\n ***************    Google Address:   *************** \n")
#
# for address1 in elements:
#     print(address1)
#     for address3 in elements[address1]:
#         print(address3['northeast'])

end_point = "https://maps.googleapis.com/maps/api/directions/json?"
api_key = "AIzaSyC56ho80KnfUqsochlmCiVDYF_VVUayiXc"
origin = input(" Where you are?: ")
destination = input(" Where do you want to go?: ")

nav_request = 'origin={0}&destination={1}&key={2}'.format(origin, destination, api_key)
req = requests.get(end_point + nav_request)


direction = req.json()
pprint.pprint(direction)

print("\n ***************    Google Routes:   *************** \n")

geocoder_status = direction['geocoder_status']
print(geocoder_status)

#
# for long in route:
#     print(long)
#     for copy in long['legs']:
#         print(copy)
#         for end in copy['steps']:
#             print(end)
#             for travel_mode in end['travel_mode']:
#                 print(travel_mode)
