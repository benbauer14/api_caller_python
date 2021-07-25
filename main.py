import requests
import json

res = requests.get(url="http://api.open-notify.org/iss-now.json")
res.raise_for_status()

print(res.json()["iss_position"])