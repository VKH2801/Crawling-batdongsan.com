import requests
import json
domain_URL = 'https://rsapi.goong.io/geocode?address='

API_key = '&api_key=22DfeaveAqw3AHJSXNFVYt4g3lUTlJ91ebcZt18B'

# address = '1 Tôn Thất Thuyết, Phường 1, Quận 4, Thành phố Hồ Chí Minh, Vietnam'

# res = requests.get(domain_URL + address + API_key)

# print(res.text)

list_properties_part1 = []
list_properties_part2 = []


with open('list_results_log_lat_formatted.json', 'r' , encoding='utf-8') as f:
    data = json.load(f)


print(range(len(data)))

for i in range(0, 901):
    address = data[i]["address"]
    res = requests.get(domain_URL + address + API_key)
    

    data_res = json.loads(res.text)

    # Lấy lat và lng
    lat = data_res['results'][0]['geometry']['location']['lat']
    lng = data_res['results'][0]['geometry']['location']['lng']

    result = {
        'price': data[i]['price'],
        'size': data[i]['size'],
        'attributes': data[i]['attribute'],
        "geometry": {
            "type": "Point",
            "coordinates": [
                str(lng),
                str(lat)
            ]
        }
    }
    list_properties_part1.append(result)
    
with open('list_results_part1.json', 'w', encoding='utf-8') as f:
    json.dump(list_properties_part1, f, ensure_ascii=False)

# for i in range(902, 1000): 
#     address = data[i]["address"]
#     res = requests.get(domain_URL + address + API_key)

#     data = json.loads(res.text)

#     # Lấy lat và lng
#     lat = data['results'][0]['geometry']['location']['lat']
#     lng = data['results'][0]['geometry']['location']['lng']

#     result = {
#         'price': data[i]['price'],
#         'size': data[i]['size'],
#         'attributes': data[i]['attribute'],
#         "geometry": {
#             "type": "Point",
#             "coordinates": [
#                 str(lng), 
#                 str(lat)
#             ]
#         }
#     }
#     list_properties_part2 = append(result)

