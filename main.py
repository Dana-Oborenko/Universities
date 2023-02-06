import requests

response = requests.get("https://raw.githubusercontent.com/Hipo/university-domains-list/master/world_universities_and_domains.json")

data = response.json()

latvijas_universitates = []

for uni in data:
    if uni["alpha_two_code"] == "LV":
        latvijas_universitates.append(uni)

# print(latvijas_universitates)

for i in latvijas_universitates:
    print(i["name"])