import requests
import json
from datetime import datetime

MY_LAT = 44.876786683641164 
MY_LONG = -93.4560947576714

parameters ={
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}
res = requests.get(url="http://api.open-notify.org/iss-now.json")
res.raise_for_status()

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(int(sunrise)-5)

if int(sunset) <= 4:
    print(int(sunset) + 19)
else:  
    print(int(sunset) - 5)

time_now = datetime.now().hour

print(time_now)



print(res.json()["iss_position"])