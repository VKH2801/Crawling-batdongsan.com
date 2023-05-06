import json


with open('list_properties_copy.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

list_properties_average = []
list_locations = []
list_locations_results = []

for index in data:
    location = index['location']
    if '.' in location:
        location = location.replace('.', '')
        list_locations.append(location)
    

for index in list_locations:
    if index not in list_locations_results:
        list_locations_results.append(index)


    
print(list_locations)