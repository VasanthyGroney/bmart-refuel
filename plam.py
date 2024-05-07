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
    radius = input("Enter a radius: ")
    fuel = input("What do you want to fuel: ")
    return location, radius, fuel


def get_all_inputs():
    phone_number = get_phone_number()  # gets phone number
    database = load_database("sms_project.json")
    found, data = check_database(phone_number, database)  # gets info if phonenumber is in database and gets data
    if found:
        user_params = {}
        for key, val in data.items():
            print(f"{key}: {val}")
            answer_choice = input(f"Do you want to use the {key}?")
            if "n" in answer_choice.lower():
                val = input(f"Enter a {key}: ")
            user_params[key] = val
        save_user_params(user_params, "sms_project.json", phone_number, database)
    location, radius, fuel = get_user_params()
    user_params = {"location": location, "radius": radius, "fuel": fuel}
    save_user_params(user_params, "sms_project.json", phone_number, database)


if __name__ == "__main__":
    get_all_inputs()