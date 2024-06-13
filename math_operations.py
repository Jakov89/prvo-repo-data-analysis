import requests
import json


get_params = {
    "num1" : 7,
    "num2" : 15,
    "operation" : "add"
}
response = requests.get(
        url = "https://4ae5-46-217-73-34.ngrok-free.app/math",
        params=get_params
)

if response.status_code == 200:
    res = json.loads(response.text)
    print(f"Rezultatot e {res['result']}")

else:
    print("Ima greshka")