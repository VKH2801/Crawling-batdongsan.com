import http.client
import urllib.parse
import json

# Đọc dữ liệu từ file JSON
with open('temp_data.json', 'r', encoding='utf=8') as input_file:
    data_json = json.load(input_file)

list_longitude_latitude = []
# Tạo file mới để lưu kết quả
with open('result_temp.json', 'w', encoding='utf-8') as outfile:
    # Lặp qua từng địa chỉ và truy vấn thông tin
    for index in data_json:
        location = index["location2"]
        print(location)
        conn = http.client.HTTPConnection('api.positionstack.com')
        params = urllib.parse.urlencode({
            'access_key': 'b35ed365b02974824db234fa58a62426',
            'query': location,
            'limit': 1,
        })
        conn.request('GET', '/v1/forward?{}'.format(params))
        res = conn.getresponse()
        data = res.read()

        # Lưu kết quả vào file mới
        json_data = json.loads(data.decode("utf-8"))
        # latitude = json_data['data'][0]["latitude"]
        # longitude = json_data['data'][0]["longitude"]
        # print('Longitude' + str(longitude) + ' Latitude' + str(latitude))
        # result = {"price": index["price"],
        #               "size": index["size"],
        #               "attribute": index['attribute'],
        #               "address": location,
        #               "longitude": str(longitude), 
        #               "latitude": str(latitude) }
        # list_longitude_latitude.append(result)
        if isinstance(json_data, list) and len(json_data) > 0:
            latitude = json_data['data'][0]["latitude"]
            longitude = json_data['data'][0]["longitude"]
            result = {"price": index["price"],
                      "size": index["size"],
                      "attribute": index['attribute'],
                      "address": location,
                      "longitude": str(longitude), 
                      "latitude": str(latitude) }
            list_longitude_latitude.append(result)
            json.dump(result, outfile, ensure_ascii=False)
            print(result)
        else:
            latitude = ''
            longitude = ''
            result = {"price": index["price"],
                      "size": index["size"],
                      "attribute": index['attribute'],
                      "address": location,
                      "longitude": longitude, 
                      "latitude": latitude }
            # list_longitude_latitude.append(result)
            json.dump(result, outfile, ensure_ascii=False)
            print(result)
            continue
    
    
with open('list_results_long_latitude_temp.json', 'w', encoding='utf-8') as outfile:
    json.dump(list_longitude_latitude, outfile, ensure_ascii=False)
    print('Done List Results Longitude Latitude')

print("Done")













