import http.client
import urllib.parse
import json

def get_coordinates(location):
    conn = http.client.HTTPConnection('api.positionstack.com')
    params = urllib.parse.urlencode({
        'access_key': 'b35ed365b02974824db234fa58a62426',
        'query': location,
        'limit': 1,
    })
    conn.request('GET', '/v1/forward?'.format(params))
    res = conn.getresponse()
    data = res.read()

    json_data = json.loads(data.decode("utf-8"))
    if isinstance(json_data, list) and len(json_data) > 0:
        latitude = json_data[0]["latitude"]
        longitude = json_data[0]["longitude"]
        return (longitude, latitude)
    else:
        return None

def get_coordinates_with_retry(location):
    result = get_coordinates(location)
    if result is None:
        return get_coordinates_with_retry(location)
    else:
        return result

with open('temp_data.json', 'r', encoding='utf=8') as input_file:
    data_json = json.load(input_file)

list_longitude_latitude = []
with open('result.json', 'w', encoding='utf-8') as outfile:
    for index in data_json:
        location = index["location2"]
        print(location)

        # Truy vấn tọa độ
        coordinates = get_coordinates_with_retry(location)
        if coordinates is not None:
            longitude, latitude = coordinates
        else:
            longitude, latitude = '', ''

        # Lưu kết quả vào file mới
        result = {"price": index["price"],
                  "size": index["size"],
                  "attribute": index['attribute'],
                  "address": location,
                  "longitude": longitude, 
                  "latitude": latitude }
        list_longitude_latitude.append(result)
        json.dump(result, outfile, ensure_ascii=False)
        print(result)

with open('list_results_long_latitude.json', 'w', encoding='utf-8') as outfile:
    json.dump(list_longitude_latitude, outfile, ensure_ascii=False)
    print('Done List Results Longitude Latitude')

print("Done")
