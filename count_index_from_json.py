import json
import http.client, urllib.parse

with open('list_properties_with_format.json', 'r', encoding='utf-8') as f:
    data = json.load(f)


locations = []
list_locations_with_longitude_latitude = []

for index in data:
    location = index['location']
    if location not in locations:
        locations.append(location)

# print(locations)
API_KEY = 'b35ed365b02974824db234fa58a62426'
LIMIT_ACCESS = 1

for INDEX in locations:
    conn = http.client.HTTPConnection('api.positionstack.com')

    params = urllib.parse.urlencode({
        'access_key': API_KEY,
        'query': INDEX,
        'limit': LIMIT_ACCESS,
    })

    conn.request('GET', '/v1/forward?{}'.format(params))

    res = conn.getresponse()
    data = res.read()


    json_data = json.loads(data.decode("utf-8"))
    print(INDEX + ': ' 'longitude ' + str(json_data['data'][0]["longitude"]) + ', ' + 'latitude ' + str(json_data['data'][0]["latitude"]))
    
    result = {
        "location": str(INDEX),
        "longitude": str(json_data['data'][0]["longitude"]),
        "latitude": str(json_data['data'][0]["latitude"])
    }
    list_locations_with_longitude_latitude.append(result)

with open('list_locations_with_longitude_latitude_for_batdongsan_com_vn.json', 'w', encoding='utf-8') as f:
    json.dump(list_locations_with_longitude_latitude, f, ensure_ascii=False)
    print("Done adding location with longitude latitude to list")




        
