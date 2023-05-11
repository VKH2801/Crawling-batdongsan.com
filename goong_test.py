import requests
import json
domain_URL = 'https://rsapi.goong.io/geocode?address='


API_key = '&api_key=22DfeaveAqw3AHJSXNFVYt4g3lUTlJ91ebcZt18B'

address = '1 Tôn Thất Thuyết, Phường 1, Quận 4, Thành phố Hồ Chí Minh, Vietnam'

res = requests.get(domain_URL + address + API_key)

print(res.text)

with open('list_properties_copy.json', 'r' , encoding='utf-8') as f:
    data = json.load(f)

# print(range(len(data)))


char_dot = '·'
# for index in range(len(data)):
#     location = data[index]['location']
#     if ():
