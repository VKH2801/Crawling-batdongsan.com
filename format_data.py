from geopy.geocoders import Nominatim
import json
app_name = 'format_data.py'


# Khởi tạo geolocator
geolocator = Nominatim(user_agent= app_name)

# Các quận trong TP. Hồ Chí Minh
districts = ["Quận 1", "Quận 2", "Quận 3", "Quận 4", "Quận 5", "Quận 6", "Quận 7", "Quận 8", "Quận 9", "Quận 10", "Quận 11", "Quận 12", "Bình Tân", "Bình Thạnh", "Gò Vấp", "Phú Nhuận", "Tân Bình", "Tân Phú", "Thủ Đức"]

# Tạo từ điển lưu tọa độ của các quận
district_coords = {}

for district in districts:
    # Lấy địa chỉ của quận
    location = geolocator.geocode(district + ", Hồ Chí Minh")
    
    # Lưu tọa độ của quận vào từ điển
    district_coords[district] = (location.longitude, location.latitude)

print(district_coords)

with open('list_district_coordinates.json', 'w', encoding='utf-8') as outfile:
    json.dump(district_coords, outfile, ensure_ascii=False)
