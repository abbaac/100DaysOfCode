import datetime as dt
import requests

class FlightData:
    
    def __init__(self, price, origin_airpot, destination_airport, out_date, return_date, nr_stops):
        self.price = price
        self.origin_airport = origin_airpot
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date        
        self.no_of_stops = nr_stops

def find_cheapest_flight(data):
    if data is None or not data['data']:
        # print("No flight data")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", "N/A")
    
    first_flight = data["data"][0]
    lowest_price = float(first_flight["price"]["grandTotal"])
    origin_code = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination_code = first_flight["itineraries"][0]["segments"][-1]["arrival"]["iataCode"]
    departure_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_date =  first_flight["itineraries"][1]["segments"][0]["arrival"]["at"].split("T")[0]
    no_of_stops = len(first_flight["itineraries"][0]["segments"])

    
    cheapest_flight = FlightData(lowest_price, origin_code, destination_code, departure_date, return_date, no_of_stops)

    for flight in data["data"]:
        price = float(flight["price"]["grandTotal"])
        if price <= lowest_price:
            lowest_price = price
            origin_code = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination_code = flight["itineraries"][0]["segments"][-1]["arrival"]["iataCode"]
            departure_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_date =  flight["itineraries"][1]["segments"][0]["arrival"]["at"].split("T")[0]
            no_of_stops = len(flight["itineraries"][0]["segments"])

            cheapest_flight = FlightData(lowest_price, origin_code, destination_code, departure_date, return_date, no_of_stops)

    return cheapest_flight
