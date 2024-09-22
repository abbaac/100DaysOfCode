import requests
import datetime as dt

USERNAME = "aaliconcern"
TOKEN = "vjkrinai$ubv&@1ibveo!eovn"
GRAPH_ID = "commit101"

pixela_endpoint = "https://pixe.la/v1/users"

params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes" 
}

# respone = requests.post(url=pixela_endpoint, json=params)
# print(respone.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "Commit Tracker",
    "unit": "commit",
    "type": "int",
    "color": "momiji" 
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# repsone = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(repsone.text)

pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

date = dt.datetime(year=2024, month=9, day=8)
formatted_date = date.strftime("%Y%m%d")

# print(now)
# new_pixel_params = {
#     "date": formatted_date,
#     "quantity": "3"

# }


# response = requests.post(url=pixel_creation_endpoint, json=new_pixel_params, headers=headers)
# print(response.text)



#Update Previous Pixel
update_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}/{formatted_date}"

update_pixel_params = {
    "quantity": "20",
}

# response = requests.put(url=update_pixel_endpoint, json=update_pixel_params, headers=headers)
# print(response.text)
    
#Delete Previous Pixel
delete_previous_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}/{formatted_date}"

response = requests.delete(url=delete_previous_pixel_endpoint, headers=headers)
print(response.text)

# request_loop = True
# while request_loop:
#     response = requests.put(url=pixel_creation_endpoint, json=update_pixel_params, headers=headers)
#     response_text = response.text
#     print(response_text)
#     if "Please retry this request." not in response_text:
#         request_loop = False
#     else:
#         print("Retry delete")