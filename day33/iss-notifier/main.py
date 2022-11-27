import requests
from datetime import datetime
import time

MY_LAT = 27.994900
MY_LONG = -82.213051

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_latitude <= MY_LONG+5:
        return True
    

def is_night():

    parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


if is_night() and is_iss_overhead():
    print('lookup')
else:
    print('not yet')
    time.sleep(60)


# BONUS: run the code every 60 seconds.



