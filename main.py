import vasanthy
import plam
import nebiel


def main():
    phone_number, user_params = plam.get_all_inputs()
    rad, fuel = user_params["radius"], user_params["fuel"]
    lng, lat = vasanthy.get_coordinates(user_params["location"])
    gasstation = nebiel.get_api_info(lat, lng, rad, fuel, "price")
    link = nebiel.get_maps_link(gasstation)
    message_1, message_2 = nebiel.write_message(gasstation, fuel, link)
    vasanthy.send_sms_user(phone_number, message_1)
    vasanthy.send_sms_user(phone_number, message_2)


if __name__ == "__main__":
    main()
