import geocoder

# Địa chỉ cần tìm vị trí
address = "Khu đô thị Thủ Thiêm, Quận 2, TP.Thủ Đức TP. Hồ Chí Minh, An Khánh, Quận 2, Thành phố Hồ Chí Minh, Vietnam"

# Sử dụng geocoder để lấy thông tin vị trí của địa chỉ
location = geocoder.osm(address)

# In ra vị trí của địa chỉ
print(location.latlng)
