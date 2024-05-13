import requests
from dotenv import load_dotenv
import os
import json


load_dotenv()


INFO_URL_BASE = os.getenv("INFO_URL_BASE")
INFO_API_KEY = os.getenv("INFO_API_KEY")
GOOGLE_MAPS_BASE = os.getenv("GOOGLE_MAPS_BASE")
BITLY_TOKEN = os.getenv("BITLY_TOKEN")
BITLY_SHORTEN_URL = os.getenv("BITLY_SHORTEN_URL")


def get_api_info(lat, lng, rad, fuel, sort):
    res = requests.get(INFO_URL_BASE + "lat=" + lat + "&lng=" + lng + "&rad=" + rad
                       + "&sort=" + sort + "&type=" + fuel + "&apikey=" + INFO_API_KEY)
    data = res.json()
    top_station = data["stations"][0]
    return top_station


def write_message(gasstation, link):
    message = (f'Top choice:\n'
               f'{gasstation["price"]}€ -- {gasstation["name"]}\n'
               f"{link}")
    return message


def get_maps_link(gasstation):
    address = (gasstation["name"] + "%2C" + gasstation["street"] +
               str(gasstation["houseNumber"]) + "%2C" + str(gasstation["postCode"])
               + gasstation["place"])
    final_address_query = address.replace(" ", "+")
    return GOOGLE_MAPS_BASE + final_address_query


def shorten_link(link):
    try:
        headers = {
            'Authorization': f'Bearer {BITLY_TOKEN}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        payload = json.dumps({
            "long_url": link
        })
        data = requests.post(BITLY_SHORTEN_URL, data=payload, headers=headers)
        response = data.json()
        short_link = response["link"]
        return short_link
    except requests.HTTPError as e:
        print("Error occurred to shorten link, continue with longer url.")
        return link
