import requests
from dotenv import load_dotenv
import os


load_dotenv()


INFO_URL_BASE = os.getenv("INFO_URL_BASE")
INFO_API_KEY = os.getenv("INFO_API_KEY")
GOOGLE_MAPS_BASE = os.getenv("GOOGLE_MAPS_BASE")


def get_api_info(lat, lng, rad, fuel, sort):
    res = requests.get(INFO_URL_BASE + "lat=" + lat + "&lng=" + lng + "&rad=" + rad
                       + "&sort=" + sort + "&type=" + fuel + "&apikey=" + INFO_API_KEY)
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
