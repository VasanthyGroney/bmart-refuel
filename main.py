import vasanthy
import plam
import nebiel


def main():
    while True:
        try:
            phone_number, user_params = plam.get_all_inputs()
            rad, fuel = user_params["radius"], user_params["fuel"]
            lng, lat = vasanthy.get_coordinates(user_params["location"])
            break
        except Exception as e:
            print(e)
            print("\n Please Try again.")
    gasstation = nebiel.get_api_info(lat, lng, rad, fuel, "price")
    link = nebiel.get_maps_link(gasstation)
    message = nebiel.write_message(gasstation, link)
    vasanthy.send_sms_user(phone_number, message)


if __name__ == "__main__":
    main()
