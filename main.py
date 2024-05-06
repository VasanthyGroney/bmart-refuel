import requests


BEGIN_URL = "https://nominatim.openstreetmap.org/search?addressdetails=1&q="
END_URL = "&format=jsonv2&limit=1"


def get_coordinates(user_address):
    address = user_address.replace(" ", "+")
    res = requests.get(BEGIN_URL + address + END_URL)
    data = res.json()
    lon = data[0].get("lon")
    lat = data[0].get("lat")
    return lon,lat

print(get_coordinates("trautaeckerstrasse 3 70567 stuttgart"))


