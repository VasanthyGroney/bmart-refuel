import requests

INFO_URL_BASE = "https://creativecommons.tankerkoenig.de/json/list.php?"
API_KEY = "8eaba7a8-c6a0-7166-8b0c-8d9f2056c212"
GOOGLE_MAPS_BASE = "https://www.google.com/maps/search/?api=1&query="


def get_api_info(lat, lng, rad, fuel, sort):
    res = requests.get(INFO_URL_BASE + "lat=" + lat + "&lng=" + lng + "&rad=" + rad
                       + "&sort=" + sort + "&type=" + fuel + "&apikey=" + API_KEY)
    data = res.json()
    top_station = data["stations"][0]
    return top_station


def write_message(gasstation, fuel, link):
    message_1 = (f'Top choice: {gasstation["name"]}\n'
                 f'Price ({fuel}): {gasstation["price"]}\n')
    message_2 = (f"Google Maps Link:\n"
                 f"{link}")
    return message_1, message_2


def get_maps_link(gasstation):
    address = (gasstation["name"] + "%2C" + gasstation["street"] +
               str(gasstation["houseNumber"]) + "%2C" + str(gasstation["postCode"])
               + gasstation["place"])
    final_address_query = address.replace(" ", "+")
    return GOOGLE_MAPS_BASE + final_address_query
