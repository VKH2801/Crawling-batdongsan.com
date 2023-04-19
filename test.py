from bs4 import BeautifulSoup
import pprint
from selenium import webdriver
import json

#Lay noi dung trang web
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

base_url = 'https://batdongsan.com.vn/nha-dat-ban-tp-hcm'

list_links_base = []
list_properties_info = []
list_districts_info = []

# # Khởi tạo đối tượng Chrome WebDriver
# driver = webdriver.Chrome('/path/to/chromedriver')

# # Truy cập trang web
# driver.get(base_url)

# # Chờ cho trang web tải hoàn tất và thông báo "just a moment..." biến mất
# driver.implicitly_wait(10)

# # Lấy nội dung của trang web
# html_content = driver.page_source

# # Tạo đối tượng BeautifulSouptừ nội dung HTML
# try : 
#     soup = BeautifulSoup(html_content, 'html.parser')
# except:
#     print("Can't connect to server url:" + base_url)


for one in range(1, 2):
    list_links_base.append(base_url + '/p' + str(one))

for index in range(len(list_links_base)) : 
    # Khởi tạo đối tượng Chrome WebDriver
    driver = webdriver.Chrome('/path/to/chromedriver')

    # Truy cập trang web
    driver.get(list_links_base[index])

    # Chờ cho trang web tải hoàn tất và thông báo "just a moment..." biến mất
    driver.implicitly_wait(10)

    # Lấy nội dung của trang web
    html_content = driver.page_source

    # Tạo đối tượng BeautifulSoup từ nội dung HTML
    try :
        soup = BeautifulSoup(html_content, 'html.parser')
    except:
        print("Can't connect to server url:" + base_url)


    prices = [i.text for i in soup.find_all('span', {'class' : 're__card-config-price js__card-config-item'})]
    acreages = [i.text for i in soup.find_all('span', {'class' : 're__card-config-area js__card-config-item'})]
    locations = [i.text for i in soup.find_all('div', {'class' : 're__card-location'})]
    prices_per_m2 = [i.text for i in soup.find_all('span', {'class' : 're__card-config-price_per_m2 js__card-config-item'})]
    char_line_break_to_remove = '\n'
    char_dot_to_remove = '.'

    for i in range(len(locations)): 
        locations[i] = locations[i].replace(char_line_break_to_remove, '')
        locations[i] = locations[i].replace(char_dot_to_remove, '')

    for i in range(len(locations)):
        try:
            if(acreages[i] == ''):
                acreages[i] = None
        except IndexError:
            acreages.append(None)

        if i >= len(acreages):
            acreages.append(None)
        else:
            if acreages[i] == '':
                acreages[i] = None
        

        
        # if i >= len(prices_per_m2):
        #     prices_per_m2.append('')
        # try:
        #     if(prices_per_m2[i] == ''):
        #         prices_per_m2[i] = None
        # except IndexError:
        #     prices_per_m2.append('')

        item = {
            "price": prices[i],
            "acreage": acreages[i],        
            "location": locations[i]
        }
        list_properties_info.append(item)

    for i in list_properties_info: 
        if (i['price'] == 'Giá thỏa thuận'): 
            list_properties_info.pop(list_properties_info.index(i))
        # if (i['price Per m2'] == ''):
        #     list_properties_info.pop(list_properties_info.index(i))


    json_data = json.dumps(list_properties_info)
    # pprint.pprint(list_properties_info)
    # pprint.pprint(prices_per_m2)
    print("============================================================")
    print(list_links_base[index])
    print("============================================================")

    

with open('list_properties_test.json', 'w', encoding='utf-8') as outfile:
    json.dump(list_properties_info, outfile, ensure_ascii=False)


