import requests
import json
domain_URL = 'https://rsapi.goong.io/geocode?address='

API_key = '&api_key=22DfeaveAqw3AHJSXNFVYt4g3lUTlJ91ebcZt18B'

# address = '1 Tôn Thất Thuyết, Phường 1, Quận 4, Thành phố Hồ Chí Minh, Vietnam'

# res = requests.get(domain_URL + address + API_key)

# print(res.text)

list_properties_part1 = []


with open('list_results_long_latitude.json', 'r' , encoding='utf-8') as f:
    data = json.load(f)

print(range(len(data)))



for i in range(1, 901):
    address = data[i]["address"]
    res = requests.get(domain_URL + address + API_key)
    

    data = json.loads(res.text)

    # Lấy lat và lng
    lat = data['results'][0]['geometry']['location']['lat']
    lng = data['results'][0]['geometry']['location']['lng']

    result = {
        'price': data[i]['price'],
        'size': data[i]['size'],
        'attributes': data[i]['attribute'],
        "geometry": {
            "type": "Point",
            "coordinates": [
                lng, lat
            ]
        }
    }
    


for i in range(902, 1000): 
    address = data[i]["address"]
    res = requests.get(domain_URL + address + API_key)

    data = json.loads(res.text)

    # Lấy lat và lng
    lat = data['results'][0]['geometry']['location']['lat']
    lng = data['results'][0]['geometry']['location']['lng']

    result = {
        'price': data[i]['price'],
        'size': data[i]['size'],
        'attributes': data[i]['attribute'],
        "geometry": {
            "type": "Point",
            "coordinates": [
                lng, lat
            ]
        }
    }

