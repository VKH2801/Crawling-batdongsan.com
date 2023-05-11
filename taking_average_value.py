import json
import requests


domain_URL = 'https://rsapi.goong.io/geocode?address='

API_key = '&api_key=22DfeaveAqw3AHJSXNFVYt4g3lUTlJ91ebcZt18B'

with open('list_properties_copy.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

list_properties_average = []
list_locations = []
location_average = {}
list_locations_average = []
list_results = []
count = 0
for i in data:
    location = i['location']
    longitude = i['longitude']
    latitude = i['latitude']
    price = i['price']

    # Chuẩn hóa kiểu dữ liệu 'giá' trong data.
    if isinstance(price, str) and 'triệu' in price:
        price = float(price.replace(' triệu', ''))

    if isinstance(price, str) and 'nghìn' in price:
        price = float(price.replace(' nghìn', ''))
        price = price / 1000

    if isinstance(price, str) and 'tỷ' in price:
        price = float(price.replace(' tỷ', '').replace(',', '.'))
        price = price * 1000

    if isinstance(price, str) and 'Giá thỏa thuận' in price:
        price = 1
    else:
        pass


    # Chuẩn hóa dữ liệu location - xóa dấu '·' và add vào list_locations.
    if '·' in location:
        location = location.replace('·', '')
        result = {
            'price': price,
            'acreage': i['acreage'],
            'location': location,
            'coordinates': [
                longitude, latitude
            ]
        }
        list_locations.append(location)

    if location in location_average:
        location_average[location]['sum'] += price
        location_average[location]['count'] += 1
        
    else:
        location_average[location] = {"sum": price, "count": 1,}
        



for location, value in location_average.items():
    location_average = value["sum"] / value['count']
    result = {
        "location": location,
        "average_price": location_average
    }
    list_properties_average.append(result)


for index in list_properties_average:
    address = index["location"]
    res = requests.get(domain_URL + address + API_key)

    data = json.loads(res.text)

    # Lấy lat và lng
    lat = data['results'][0]['geometry']['location']['lat']
    lng = data['results'][0]['geometry']['location']['lng']

    result = {
        "location": location,
        "average_price": location_average,
        "geometry": {
            "type": "Point",
            "coordinates": [
                lng, lat
            ]
        }
    }
    list_results.append(result)

with open('list_properties_average.json', 'w', encoding='utf-8') as f:
    json.dump(list_results, f, ensure_ascii=False)


# print(list_properties_average)