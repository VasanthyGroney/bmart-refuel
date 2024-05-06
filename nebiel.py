import requests


API_BASE = "https://creativecommons.tankerkoenig.de/json/detail.php?"
API_KEY = "8eaba7a8-c6a0-7166-8b0c-8d9f2056c212"


def get_api_info(lat, lng, rad, fuel, sort):
    res_rad = requests.get(API_BASE + "lat=" + lat + "&lng=" + lng + "&rad=" + rad
                           + "&sort=" + sort + "&type=" + fuel + "&apikey=" + API_KEY)
    data = res_rad.json()
    useful_stations = []
    for station in data["stations"]:
        if station["isOpen"]:
            useful_stations.append(station)
    print(useful_stations)
    res_detail = requests.get(API_BASE + "id=" + data["stations"][0]["id"] + "&apikey=" + API_KEY)
    data_detail = res_detail.json()
    return useful_stations[:3], data_detail


get_api_info("52.516181", "13.376935", "5", "e5", "price")
