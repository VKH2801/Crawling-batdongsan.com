import json
import random



with open('list_result.json', 'r', encoding='utf-8') as f:
    data_input = json.load(f)

list_result = []

for i in range(len(data_input)):
    price = data_input[i]['price']
    rent__ = price.replace('.', '')
    rent_ = rent__.replace('₫', '')
    rent = float(rent_)
    type = data_input[i]['attributes']
    id = 'item-' + str(i + 1)
    title = data_input[i]['attributes']
    except_ = data_input[i]['address']
    description = data_input[i]['address']
    area_temp = data_input[i]['size']
    area_ = area_temp.replace(' sq m', '')
    area = float(area_.replace(',', ''))
    deposit = rent
    rooms = random.randint(1, 4)
    type_geometry = data_input[i]['geometry']['type']
    coordinates = data_input[i]['geometry']['coordinates']

    item = {
        'type': 'Feature',
        'properties': {
            'id': id,
            'title': title,
            'except': except_,
            'description': description,
            "images": [{
                        "original": "/assets/images/original/apartment/3/1.jpg",
                        "thumbnail": "/assets/images/thumbnail/apartment/3/1.jpg"
                    },
                    {
                        "original": "/assets/images/original/apartment/3/2.jpg",
                        "thumbnail": "/assets/images/thumbnail/apartment/3/2.jpg"
                    },
                    {
                        "original": "/assets/images/original/apartment/3/3.jpg",
                        "thumbnail": "/assets/images/thumbnail/apartment/3/3.jpg"
                    }
            ],
            'type': type,
            'rooms': rooms,
            'area': area,
            'rent': rent,
            'deposit': deposit,
        },
        'geometry': {
            'type': type_geometry,
            'coordinates': coordinates,
        }
    }
    list_result.append(item)

    
with open('list_result_standardized.json', 'w', encoding='utf-8') as f:
    json.dump(list_result, f, ensure_ascii=False)
