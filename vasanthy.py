import requests
import json
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Access environment variables
COORD_BASE_URL = os.getenv("COORD_BASE_URL")
COORD_API_KEY = os.getenv("COORD_API_KEY")
SMS_BASE_URL = os.getenv("SMS_BASE_URL")
AUTHORIZATION = os.getenv("AUTHORIZATION")


def get_coordinates(user_address):
    address = user_address.replace(" ", "+")
    res = requests.get(COORD_BASE_URL + address + "&api_key=" + COORD_API_KEY)
    data = json.loads(res.text)
    lon = data[0].get("lon")
    lat = data[0].get("lat")
    return lon, lat


def send_sms_user(phone_number, message):
    try:
        headers = {
            'Authorization': AUTHORIZATION,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        payload = json.dumps({
            "messages": [
                {
                    "destinations": [
                        {
                            "to": phone_number
                        }
                    ],
                    "from": "B-Smart RFL",
                    "text": message
                }
            ]
        })
        data = requests.post(SMS_BASE_URL, data=payload, headers=headers)
        response = data.text
        print("Message successfully send.")
    except requests.HTTPError as e:
        print(e)
