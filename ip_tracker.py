import requests
import re
import json
import os
from urllib.request import urlopen

ip = input("Enter the ip:")
value = {'ip': ip}
r = requests.post('https://ipinfo.io', data=value)
print("<<<<<<<<<<<<<<<<<<<<<<<[ "+ip+" DETAILS ]>>>>>>>>>>>>>>>>>>>>>>>")
print("                                                      by S4MUR41")
print("\n")
r_dict = r.json()
city = r_dict['city']
region = r_dict['region']
country = r_dict['country']
location = r_dict['loc']
location = location.split(",")
latitude = location[0]
longitude = location[1]
organization = r_dict['org']
postal_code = r_dict['postal']
timezone = r_dict['timezone']

print("City: ",city)
print("Region: ",region)
print("Country: ",country)
print("Location: ",r_dict['loc'])
print("Organization: ",organization)
print("Postal code: ",postal_code)
print("Timezone: ",timezone)
print("\n")

api_key="mWkstMBDegSRHvqLeHVLxoBGAAvvnfH7"
url2 = "https://www.mapquestapi.com/staticmap/v5/map?key="+api_key+"&center="+latitude+","+longitude+"&size=@2x"
static_map = requests.get(url2)

with open("static_map.jpeg","wb") as f:
    f.write(static_map.content)

os.system("static_map.jpeg")
