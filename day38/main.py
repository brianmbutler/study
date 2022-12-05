import os
import requests
from datetime import datetime

APP_ID = os.environ.get('nutronix_app_id')
KEY = os.environ.get('nutronix_api')	
EXERCISE_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
TODAY = datetime.now()
SHEETY_ENDPOINT = os.environ.get('sheety_workout_endpoint')


headers = {
    'x-app-id': APP_ID,
    'x-app-key': KEY,
    'Content-Type': "application/json"
}

body = {
 "query":"ran 3 miles",
 "gender":"male",
 "weight_kg":95.25,
 "height_cm":177.8,
 "age":44
}

response = requests.post(url = EXERCISE_ENDPOINT, headers = headers, json=body)
data = response.json()['exercises']
exercise = data[0]['name'].capitalize()
calories = round(data[0]['nf_calories'])
duration = round(data[0]['duration_min'])

today = datetime.strftime(TODAY,f'%d/%m/%Y')
time = datetime.strftime(TODAY,f'%H:%m')

sheety_body = {
    'workout': {
        'date': today,
        'time': time, 
        'exercise': exercise,
        'duration': duration,
        'calories': calories,
    }
}

upload_to_sheety = requests.post(url=SHEETY_ENDPOINT,json=sheety_body)
print(upload_to_sheety.text)