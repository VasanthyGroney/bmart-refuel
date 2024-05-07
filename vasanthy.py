import requests
import json


BEGIN_URL = "https://nominatim.openstreetmap.org/search?addressdetails=1&q="
END_URL = "&format=jsonv2&limit=1"


def get_coordinates(user_address):
    address = user_address.replace(" ", "+")
    res = requests.get(BEGIN_URL + address + END_URL)
    data = json.loads(res.text)
    lon = data[0].get("lon")
    lat = data[0].get("lat")
    return lon,lat
#except Exception as e:
       # print(f'An error occurred while attempting to send SMS message to "{number}" (message: "{msg}"). \nError: ', e)
print(get_coordinates("trautaeckerstrasse 3 70567 stuttgart"))


