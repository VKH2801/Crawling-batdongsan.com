from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="test_lay_ten_duong.py")

# Địa chỉ cần lấy tọa độ
address = "Khu đô thị Thủ Thiêm, Quận 2, TP.Thủ Đức TP. Hồ Chí Minh, An Khánh, Quận 2, Thành phố Hồ Chí Minh, Vietnam"

# Sử dụng geolocator để lấy tọa độ vĩ độ và kinh độ của địa chỉ trên
location = geolocator.geocode(address)

# if location is not None:
#     print((location.latitude, location.longitude))
# else:
#     print("Không tìm thấy địa chỉ")

print((location.latitude, location.longitude))