import datetime as dt
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

data_manager = DataManager()
flight_searcher = FlightSearch()
sheet_data = data_manager.get_data()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LON"

for record in sheet_data:
    if record["iataCode"] == "":
        code = flight_searcher.get_destination_code(record["city"])
        data_manager.update_data(code, record["id"])

print(f"sheet_data:\n {sheet_data}")

customer_email_sheet = data_manager.get_customer_emails()
print(customer_email_sheet)
customer_emails = [user['whatIsYourEmailAddress?'] for user in customer_email_sheet]

today = dt.datetime.today()
tommorow = (today + dt.timedelta(days=1))
six_months = (today + dt.timedelta(days=180))


for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flight = flight_searcher.check_flights(
        origin_city_code=ORIGIN_CITY_IATA,
        destination_city_code=destination["iataCode"],
        from_time=tommorow,
        to_time=six_months
    )

    cheapest_flight = find_cheapest_flight(flight)
    if cheapest_flight.price == "N/A":
            print("No direct flights found. Now searchng for connection flights...")
            flight = flight_searcher.check_flights(
            origin_city_code=ORIGIN_CITY_IATA,
            destination_city_code=destination["iataCode"],
            from_time=tommorow,
            to_time=six_months,
            is_direct=False
        )
            cheapest_flight = find_cheapest_flight(flight)
            if cheapest_flight.price == "N/A":
                print("No connection flights found. Check again another time.")
    if cheapest_flight.price != "N/A" and cheapest_flight.price <= destination["lowestPrice"]:
        print(f"Lower price flight found to {destination['city']}!")
        if cheapest_flight.no_of_stops > 1:
             message_body=f"Subject: Low price alert! Only GBP {cheapest_flight.price} to fly from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport} with {cheapest_flight.no_of_stops} stop(s)\nFly from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport} on {cheapest_flight.out_date} until {cheapest_flight.return_date} with {cheapest_flight.no_of_stops} stop(s) included."
        else:
             message_body=f"Subject: Low price alert! Only GBP {cheapest_flight.price} to fly from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport} \nFly from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport} on {cheapest_flight.out_date} until {cheapest_flight.return_date}."

        notification_manager.send_mail(
            mailing_list=customer_emails,
            message_body=message_body
        )
             
    print(f"{destination['city']}: GBP {cheapest_flight.price}")