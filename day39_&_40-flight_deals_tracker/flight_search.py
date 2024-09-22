import requests
from dotenv import load_dotenv
import os
import datetime as dt
import json

load_dotenv()

class FlightSearch:
    def __init__(self):
        self._api_key = os.getenv("AMADEUS_API_KEY")
        self._api_secret = os.getenv("AMADEUS_API_SECRET")
        self._token = self._get_new_token()
        self.endpoint = os.getenv("SHEETY_ENDPOINT_PRICES")


    def _get_new_token(self):
        
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        body = {
            "grant_type" : "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret
        }

        response = requests.post(url="https://test.api.amadeus.com/v1/security/oauth2/token", data=body, headers=header)
        response.raise_for_status()

        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()['access_token']

    def get_destination_code(self, city):

        headers = {"Authorization": f"Bearer {self._token}"}

        params = {
            "keyword": city,
            "max": "2",
            "include": "AIRPORTS"
        }
        response = requests.get(url="https://test.api.amadeus.com/v1/reference-data/locations/cities", 
                                params=params, 
                                headers=headers)
        print()
        
        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city}.")
            return "Not Found"

        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time, is_direct=True):

        headers = {"Authorization": f"Bearer {self._token}"}

        params = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "nonStop": "true" if is_direct else "false",
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "currencyCode": "GBP",
            "max": "250",
        }

        # print(f"Getting flights for {city}...")
        response = requests.get(
            url="https://test.api.amadeus.com/v2/shopping/flight-offers", 
            params=params, 
            headers=headers
        )

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            return None
        
        return response.json()

today = dt.datetime.today()
six_months = (today + dt.timedelta(days=180))

# obj = FlightSearch()
# data = obj.check_flights(origin_city_code="BOS", destination_city_code="PAR", from_time=dt.date(year=2024, month=9, day=22), to_time=six_months)
# print(json.dumps(data))

