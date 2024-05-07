import requests

API_BASE = "https://creativecommons.tankerkoenig.de/json/list.php?"
API_KEY = "8eaba7a8-c6a0-7166-8b0c-8d9f2056c212"


def get_api_info(lat, lng, rad, fuel, sort):
    res_rad = requests.get(API_BASE + "lat=" + lat + "&lng=" + lng + "&rad=" + rad
                           + "&sort=" + sort + "&type=" + fuel + "&apikey=" + API_KEY)
    data = res_rad.json()
    useful_stations = []
    for station in data["stations"]:
        if station["isOpen"]:
            useful_stations.append(station)
    return useful_stations[:3]


def write_message(gasstations):
    message = 'Our recommendation:\n'
    for station in gasstations:
        message += (f"{station["name"]}\n"
                    f"For redirection click Link:\n"
                    f"LINK\n\n")
    return message


print(get_api_info("52.516181", "13.376935", "5", "e5", "price"))
print(write_message(get_api_info("52.516181", "13.376935", "5", "e5", "price")))