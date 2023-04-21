from bs4 import BeautifulSoup
import pprint
from selenium import webdriver
import json


class WebDriverAdapter:
    def __init__(self, webdriver):
        self.webdriver = webdriver

    def get_html_content(self, url):
        self.webdriver.get(url)
        self.webdriver.implicitly_wait(10)
        html_content = self.webdriver.page_source
        return html_content


#Lay noi dung trang web
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

base_url = 'https://batdongsan.com.vn/nha-dat-ban-tp-hcm'

list_links_base = []
list_properties_info = []
list_districts_info = []


for one in range(1, 4):
    list_links_base.append(base_url + '/p' + str(one))

for index in range(len(list_links_base)) : 
    # Khởi tạo đối tượng Chrome WebDriver
    webdriver_adapter = WebDriverAdapter(webdriver.Chrome('/path/to/chromedriver'))
    # Truy cập trang web
    html_content = webdriver_adapter.get_html_content(list_links_base[index])

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

        item =  {
            "price": prices[i],
            "acreage": acreages[i],        
            "location": locations[i]
        }
        list_properties_info.append(item)
    
    for i in list_properties_info: 
        if (i['price'] == 'Giá thỏa thuận'): 
            list_properties_info.pop(list_properties_info.index(i))

    json_data = json.dumps(list_properties_info)
    # pprint.pprint(list_properties_info)
    # pprint.pprint(prices_per_m2)
    print("============================================================")
    print(list_links_base[index])
    print("============================================================")


with open('list_properties_with_format.json', 'w', encoding='utf-8') as outfile:
    json.dump(list_properties_info, outfile, ensure_ascii=False)
