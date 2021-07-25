import requests
from datetime import datetime

MY_LAT = 44.876786683641164 
MY_LONG = -93.4560947576714

parameters ={
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}
#ISS location
res = requests.get(url="http://api.open-notify.org/iss-now.json")
res.raise_for_status()

iss_lat = float(res.json()["iss_position"]["latitude"])
iss_long = float(res.json()["iss_position"]["longitude"])

def isOverHead():
    #This program assumes the ISS is overhead if the ISS lat and long are +/-5 from my location
    if(datetime.now().hour < sunrise or datetime.now().hour > sunset):
        if(abs(iss_lat - MY_LAT) < 5 and  abs(iss_long - MY_LONG)):
            return True
        else:
            return False
    else:
        return "It is daytime so it is too light to see the ISS"

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
#find hour of sunrise and sunset
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) - 5
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

if int(sunset) <= 4:
    sunset = (int(sunset) + 19)
else:  
    sunset = (int(sunset) - 5)

time_now = datetime.now().hour

print(isOverHead())



