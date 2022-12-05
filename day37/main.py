import requests
from datetime import datetime
import os

PIXELA_ENDPOINT = ' https://pixe.la/v1/users'
USERNAME = 'brianmbutler'
TOKEN = os.environ.get('pixela_token')
ID = 'graph1'


user_parameters = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_parameters)
# print(response.text)

graph_endpoint = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs'


graph_parameters = {
    'id':ID,
    'name': 'StudyTime',
    'unit': 'min',
    'type': 'float',
    'color': 'sora',
    'timezone': 'America/New_York'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(response.text)

today =  datetime.today().strftime('%Y%m%d')
quantity = '90'

pixel_parameters = {
    'date': today,
    'quantity': quantity
}
# response = requests.post(url=pixel_endpoint, json=pixel_parameters, headers=headers)
# print(response.text)

pixel_endpoint = f'{graph_endpoint}/{ID}/{today}'

response = requests.post(url=pixel_endpoint, json=pixel_parameters, headers=headers)
print(response.text)
