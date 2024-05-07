import json
from math import radians, sin, cos, sqrt, atan2

def load_fuel_stations(filename):
    with open(filename, 'r') as file:
        return json.load(file)


def calculate_distance(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = 6371 * c

    return distance


def search_fuel_stations(fuel_stations, location, radius):
    location_lat, location_lon = map(float, location.split(','))
    results = []
    for station in fuel_stations:
        station_lat, station_lon = station['coordinates']['latitude'], station['coordinates']['longitude']
        distance = calculate_distance(location_lat, location_lon, station_lat, station_lon)
        if distance <= radius:
            results.append(station)
    return results


def search_nearby_fuel_stations():
    fuel_stations = load_fuel_stations('sms_project.json')

    phone = input("Enter your phone number: ")
    location = input("Enter your location: ")
    fuel_type = input("Enter the type of fuel (gasoline/diesel/electric): ")
    radius = int(input("Enter the search radius (in km): "))

    search_results = search_fuel_stations(fuel_stations, location, radius)
    print("Search Results:")
    for result in search_results:
        print(result)


if __name__ == "__main__":
    search_nearby_fuel_stations()
