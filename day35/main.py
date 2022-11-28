import requests
import os
from twilio.rest import Client

OWM_endpoint = 'https://api.openweathermap.org/data/2.5/forecast/'
weather_api_key = os.environ.get('Open_weather_api_key')
account_sid = os.environ.get('TWILIO_ACCOUNT_SID') 
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')  
my_twilio = os.environ.get('my_twilio')


params = {
    'appid': weather_api_key,
    'lat': 27.996997261017484,
    'lon': -82.23185464659926
}

response = requests.get(url = OWM_endpoint, params=params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data['list'][7:19]

will_rain = False

for hourly_data in weather_slice:
    condition_code = hourly_data['weather'][0]['id']

    if int(condition_code) <= 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body= f"It's going to rain, bring an umbrella",
    from_ = my_twilio,
    to = '+14108080592'
    )


