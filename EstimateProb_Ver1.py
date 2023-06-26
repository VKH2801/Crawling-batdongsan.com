import requests
from bs4 import BeautifulSoup

url = 'https://mogi.vn/gia-nha-dat'

# Gửi yêu cầu HTTP GET để tải trang web
response = requests.get(url)

# Kiểm tra xem yêu cầu thành công hay không (status code 200 là thành công)
if response.status_code == 200:
    # Sử dụng BeautifulSoup để phân tích cú pháp HTML của trang web
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Tìm các phần tử HTML chứa thông tin dữ liệu bạn muốn crawl
    # và trích xuất dữ liệu từ các phần tử đó
    print('Connected')
else:
    print('Failed to retrieve data from the website.')
