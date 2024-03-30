import requests
import json

response = requests.get("https://open.er-api.com/v6/latest/USD")
if response.status_code == 200:
    result = json.loads(response.text)
    for k,v in result["rates"].items():
        print(k+" = "+str(v))
else:
    print("SERVER NOT UP TO GET RESPONSE")