import requests
import json


COORD_BASE_URL = "https://geocode.maps.co/search?q="
API_KEY = "663b3080937e8329575847yan7279cb"
SMS_BASE_URL = 'https://43l848.api.infobip.com/sms/2/text/advanced'
AUTHORIZATION = 'App 3dec643d54c66b6fab8fbfcce32f8081-27aba670-39dd-40be-8371-0f5acd088797'


def get_coordinates(user_address):
    address = user_address.replace(" ", "+")
    res = requests.get(COORD_BASE_URL + address + "&api_key=" + API_KEY)
    data = json.loads(res.text)
    lon = data[0].get("lon")
    lat = data[0].get("lat")
    return lon, lat


def send_sms_user(phone_number, message):
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
                "from": "B-Smart Refuel",
                "text": message
            }
        ]
    })
    data = requests.post(SMS_BASE_URL, data=payload, headers=headers)
    response = data.text
    print("message sent")
