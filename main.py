import requests

def myFunc(e):
    return e["name"]

response = requests.get("http://universities.hipolabs.com/search?country=latvia")

data = response.json()

data.sort(key=myFunc)

for i in range(0, len(data), 2):
    print(data[i]["name"])
