import requests 
import json
import pandas as pd 

respons = requests.get(url="http://api.open-notify.org/astros.json")

print(respons.status_code)
if respons.status_code == 200:
    print("Requestot e uspeshen")
    resp_dict = json.loads(respons.text)   
    list_of_astronauts = resp_dict["people"]
    df_astro = pd.DataFrame(list_of_astronauts)   
    df_astro.to_csv("ast.csv",index=False,encoding="utf-8")
    print("Fajlot e zapishan")
    #for astronaut in list_of_astronauts:
     #   print(f'Name: {astronaut['name']},Craft: {astronaut['craft']}')
else:
    print("Nastana Greshka")