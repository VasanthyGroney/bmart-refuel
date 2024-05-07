import requests
import json
import http.client


BEGIN_URL = "https://nominatim.openstreetmap.org/search?addressdetails=1&q="
END_URL = "&format=jsonv2&limit=1"
SMS_BASE_URL = 'https://43l848.api.infobip.com/sms/2/text/advanced'
AUTHORIZATION = 'App 3dec643d54c66b6fab8fbfcce32f8081-27aba670-39dd-40be-8371-0f5acd088797'

def get_coordinates(user_address):
    address = user_address.replace(" ", "+")
    res = requests.get(BEGIN_URL + address + END_URL)
    data = json.loads(res.text)
    lon = data[0].get("lon")
    lat = data[0].get("lat")
    return lon,lat
#except Exception as e:
       # print(f'An error occurred while attempting to send SMS message to "{number}" (message: "{msg}"). \nError: ', e)



def send_sms_user(phone_number, message, request_headers=None):
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
                "from": "InfoSMS",
                "text": message
            }
        ]
    })

    data = requests.post(SMS_BASE_URL, data=payload, headers=request_headers)
    response = data.text
    data = response.read()


    print(data.decode("utf-8"))







