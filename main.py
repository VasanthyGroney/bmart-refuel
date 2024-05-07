import vasanthy
import plam
import nebiel


def main():
    phone_number, user_params = plam.get_all_inputs()
    rad, fuel = user_params["radius"], user_params["fuel"]
    lng, lat = vasanthy.get_coordinates(user_params["location"])
    gasstations = nebiel.get_api_info(lat, lng, rad, fuel, "price")
    message = nebiel.write_message(gasstations, fuel)
    vasanthy.send_sms_user(phone_number, message)


if __name__ == "__main__":
    main()
