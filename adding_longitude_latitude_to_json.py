import json

with open('list_properties.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# with open('list_properties_copy.json', 'w', encoding='utf-8') as f:
#     json.dump(data, f, ensure_ascii=False)


list_properties_with_longitude_latitude = []

with open('list_locations_with_longitude_latitude_for_batdongsan_com_vn.json', 'r', encoding='utf-8') as f:
    data_longitude_latitude = json.load(f)

for index in data:
    for index_longitude_latitude in data_longitude_latitude:
        if index['location'] == index_longitude_latitude['location']:
            index['longitude'] = index_longitude_latitude['longitude']
            index['latitude'] = index_longitude_latitude['latitude']
            list_properties_with_longitude_latitude.append(index)
            break

with open('list_properties_copy.json', 'w', encoding='utf-8') as f:
    json.dump(list_properties_with_longitude_latitude, f, ensure_ascii=False)
