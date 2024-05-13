import json


def get_phone_number():
    return input("Enter your phone number: ")


def load_database(filename):
    with open(filename, 'r') as file:
        return json.load(file)


def check_database(phone_number, database):
    if phone_number in database:
        found = True
        data = database[phone_number]
    else:
        found = False
        data = None
    return found, data


def save_user_params(user_params, filename, phone_number, database):
    database[phone_number] = user_params
    with open(filename, 'w') as file:
        return json.dump(database, file)


def get_user_params():
    location = input("Enter your address: ")
    while True:
        radius = input("Enter a radius in km (max. 25): ")
        if 0 < int(radius) <= 25:
            break
        print("You have entered a wrong radius.\nTry again.")
    while True:
        fuel = input("What do you want to fuel? \n(Enter 'e5', 'e10' or 'diesel'): ")
        if fuel in ['e5', 'e10', 'diesel']:
            break
        print("Wrong fuel type.\nTry again")
    return location, radius, fuel


def get_all_inputs():
    phone_number = get_phone_number()  # gets phone number
    database = load_database("sms_project.json")
    found, data = check_database(phone_number, database)
    if found:
        user_params = {}
        for key, val in data.items():
            print(f"Your previous {key} was: {val}")
            answer_choice = input(f"Do you want to use the same {key}?\nEnter 'y' for yes: ")
            if "y" != answer_choice.lower():
                val = input(f"Enter a new {key}: ")
            user_params[key] = val
        save_user_params(user_params, "sms_project.json", phone_number, database)
        return phone_number, user_params
    location, radius, fuel = get_user_params()
    user_params = {"location": location, "radius": radius, "fuel": fuel}
    save_user_params(user_params, "sms_project.json", phone_number, database)
    return phone_number, user_params