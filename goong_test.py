import requests
import json
domain_URL = 'https://rsapi.goong.io/geocode?address='

API_key = '&api_key=22DfeaveAqw3AHJSXNFVYt4g3lUTlJ91ebcZt18B'
API_key_2 = '&api_key=6xCmf3dHSjPRTdALlzI3olbVbsadP71du26JQqvK'
API_key_3 = '&api_key=dxuOP76IL1ZeHTtQj48ltl1wf009m58nH2q4dXhG'
API_key_4 = '&api_key=HRGqehYPf52NT7AmFBD8biJMpNjk0AaLLv3YXA5q'

# address = '1 Tôn Thất Thuyết, Phường 1, Quận 4, Thành phố Hồ Chí Minh, Vietnam'

# res = requests.get(domain_URL + address + API_key)

# print(res.text)

list_properties_part1 = []
list_properties_part2 = []


with open('list_results_log_lat_formatted.json', 'r' , encoding='utf-8') as f:
    data = json.load(f)

with open('list_results_part2.json', 'r', encoding='utf-8') as f:
    data_part1 = json.load(f)

with open('list_results_part3.json', 'r', encoding='utf-8') as f:
    data_part2 = json.load(f)

list_result = []

for i in range(len(data_part1)):
    result = {
        'price' : data_part1[i]['price'],
        'size' : data_part1[i]['size'],
        'attributes': data_part1[i]['attributes'],
        'address': data_part1[i]['address'],
        'geometry': {
            'type': data_part1[i]['geometry']['type'],
            'coordinates': data_part1[i]['geometry']['coordinates']
        }
    }
    print(result)
    list_result.append(result)

for i in range(len(data_part2)):
    
    result = {
        'price' : data_part1[i]['price'],
        'size' : data_part1[i]['size'],
        'attributes': data_part1[i]['attributes'],
        'address': data_part1[i]['address'],
        'geometry': {
            'type': data_part1[i]['geometry']['type'],
            'coordinates': data_part1[i]['geometry']['coordinates']
        }
    }
    list_result.append(result)

with open('list_result.json', 'w', encoding='utf-8') as f:
    json.dump(list_result, f, ensure_ascii=False)

# for i in range(0, 901):
#     address = data[i]["address"]
#     res = requests.get(domain_URL + address + API_key)
    

#     data_res = json.loads(res.text)

#     # Lấy lat và lng
#     lat = data_res['results'][0]['geometry']['location']['lat']
#     lng = data_res['results'][0]['geometry']['location']['lng']

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
#     list_properties_part1.append(result)
    
# with open('list_results_part1.json', 'w', encoding='utf-8') as f:
#     json.dump(list_properties_part1, f, ensure_ascii=False)

# for i in range(1000, 1950): 
#     address = data[i]["address"]
#     res = requests.get(domain_URL + address + API_key_4)

#     data_res = json.loads(res.text)
    
#     # Lấy lat và lng
#     lat = data_res['results'][0]['geometry']['location']['lat']
#     lng = data_res['results'][0]['geometry']['location']['lng']
    

#     result = {
#         'price': data[i]['price'],
#         'size': data[i]['size'],
#         'attributes': data[i]['attribute'],
#         'address': data[i]['address'],
#         "geometry": {
#             "type": "Point",
#             "coordinates": [
#                 str(lng), 
#                 str(lat)
#             ]
#         }
#     }
#     print(result)
#     list_properties_part2.append(result)

# with open('list_results_part3.json', 'w', encoding='utf=8') as f:
#     json.dump(list_properties_part2, f, ensure_ascii=False)
#     print('Done adding list results part 3')



