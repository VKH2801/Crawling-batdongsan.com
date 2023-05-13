import json
import http.client, urllib.parse
import requests

with open('list_properties.json', 'r', encoding='utf-8') as f:
    data = json.load(f)


locations = []
list_locations_with_longitude_latitude = []
list_locations = []

for index in data:
    location = index['location']

    # Chuẩn hóa dữ liệu location - xóa dấu '·' và add vào list_locations.
    if '·' in location:
        location = location.replace('·', '')
        list_locations.append(location)
    

for i in list_locations:
    if i not in locations:
        locations.append(i)

print(locations)

domain_URL = 'https://rsapi.goong.io/geocode?address='

API_key = '&api_key=22DfeaveAqw3AHJSXNFVYt4g3lUTlJ91ebcZt18B'

for INDEX in locations:
    res = requests.get(domain_URL + str(INDEX) + API_key)

    response_data = json.loads(res.text)

    # Lấy lat và lng
    lat = response_data['results'][0]['geometry']['location']['lat']
    lng = response_data['results'][0]['geometry']['location']['lng']
    
    result = {
        "location": str(INDEX),
        "longitude": lng,
        "latitude": lat
    }
    print(result)
    list_locations_with_longitude_latitude.append(result)

with open('list_locations_with_longitude_latitude_for_batdongsan_com_vn.json', 'w', encoding='utf-8') as f:
    json.dump(list_locations_with_longitude_latitude, f, ensure_ascii=False)
    print("Done adding location with longitude latitude to list")




        
