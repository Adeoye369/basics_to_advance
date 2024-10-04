import requests
from datetime import datetime

TOKEN = "234sfosdwao3402"
USERNAME = "adeoye"
GRAPH_ID = "code1"

header_info ={
    "X-USER-TOKEN": TOKEN} 


# Making a POST request to create user
PIXELA_ENDPOINT="https://pixe.la/v1/users"
user_params= {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"}
# response = requests.post(url=f"{PIXELA_ENDPOINT}", json=user_params)
# print(response.text)



# Making a POST to create a new graph
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_params = {
    "id":GRAPH_ID,
    "name":"Coding Hours",
    "unit": "hrs",
    "type": "float",
    "color":"sora"}
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=header_info)
# print(response.text)



# Making another post request to create the pixel points
pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()
pixel_data={
    "date": today.strftime("%Y%m%d"),
    "quantity": "4.0",
}
# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=header_info)
# print(response.text)


# Making a PUT Requests
that_day = datetime(year=2024, month=7, day=27)
update_endpont = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{that_day.strftime('%Y%m%d')}"
new_pixel_data ={"quantity":"7.6"}
response = requests.put(url=update_endpont, json=new_pixel_data, headers=header_info)
print(response.text)

# Making a DELETE Request
delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{that_day.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_endpoint, json=new_pixel_data, headers=header_info)
# print(response.text)