import requests
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()

# header = {
#             "Authorization": os.getenv("SHEETY_TOKEN")
#         }

class DataManager:
    def __init__(self) -> None:
        self.sheety_token = os.getenv("SHEETY_TOKEN")
        self.sheety_endpoint_users = os.getenv("SHEETY_ENDPOINT_USERS")
        self.sheety_endpoint_prices = os.getenv("SHEETY_ENDPOINT_PRICES")        
        self.destination_data = {}
        self.users = []

    def get_data(self):
        header = {
            "Authorization": self.sheety_token
        }
        response = requests.get(url=self.sheety_endpoint_prices, headers=header)
        response.raise_for_status() 
        self.destination_data = response.json()["prices"]
        # pprint(data["prices"])
        return self.destination_data
    
    def update_data(self, code, id):
        for city in self.destination_data:
            new_data = {
                "price":{
                "iataCode": code
            }
            }

        headers = {
            "Authorization": self.sheety_token
        }

        response = requests.put(url=f"{self.sheety_endpoint_prices}/{id}", 
                                json=new_data,  
                                headers=headers)
        response.raise_for_status()
        print(response.text)

    def get_customer_emails(self):
        header = {
            "Authorization": self.sheety_token
        }
        response = requests.get(url=self.sheety_endpoint_users, headers=header)
        response.raise_for_status() 
        data = response.json()['users']
        # pprint(data["prices"])
        return data
        
# obj = DataManager()
# print(obj.get_customer_emails())