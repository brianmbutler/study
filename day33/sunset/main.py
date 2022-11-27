import requests
from datetime import datetime

long = -82.23183318892835
lat = 27.996959367955853

# response = requests.get(url=f'https://api.sunrise-sunset.org/json?lat={lat}&lng={long}')

params = {
    'lat': lat,
    'long': long,
    'formatted': 0
}

response = requests.get(url='https://api.sunrise-sunset.org/json', params=params)
data = response.json()

sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])

now = datetime.now().hour

# if now > sunset:
#     print('nighttime')
# else:
#     print('daytime')


print(sunrise)