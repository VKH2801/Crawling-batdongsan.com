from bs4 import BeautifulSoup
import re
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

base_url = 'https://search.savills.com/list?SearchList=Id_343+Category_RegionCountyCountry&Tenure=GRS_T_B&SortOrder=SO_PCDD&Currency=GBP&ResidentialSizeUnit=SquareFeet&LandAreaUnit=Acre&SaleableAreaUnit=SquareMeter&Category=GRS_CAT_RES&Shapes=W10&CurrentPage='


dong_pattern = re.compile(r'₫')
usd_vnd_exchange_rate = 24820
list_properties_info = []
list_districts_info = []


for index in range(1, 148) : 
    link_index = base_url + str(index)
    # Khởi tạo đối tượng Chrome WebDriver
    webdriver_adapter = WebDriverAdapter(webdriver.Chrome('/path/to/chromedriver'))
    # Truy cập trang web
    html_content = webdriver_adapter.get_html_content(link_index)

    # Tạo đối tượng BeautifulSoup từ nội dung HTML
    try :
        soup = BeautifulSoup(html_content, 'html.parser')
    except:
        print("Can't connect to server url:" + link_index)

    
    prices = [i.text for i in soup.find_all('span', {'class' : ['sv-property-price__value']})]
    sizes = [i.text for i in soup.find_all('div', {'class' : 'sv--size'})]
    property_attribute_values = [i.text for i in soup.find_all('div', {'class' : 'sv--residential'})]
    locations1 = [i.text for i in soup.find_all('span', {'class' : 'sv-details__address1--truncate'})]
    locations2 = [i.text for i in soup.find_all('p', {'class' : 'sv-details__address2'})]
    char_deleted_for_prices = '\xa0'
    char_usd_value = '$'
    if(prices != None):
        for i in range(len(prices)):
            if('$' in prices[i]):
                usd_value = prices[i].replace(char_usd_value, '').replace(',','')
                vnd_value = int(float(usd_value) * usd_vnd_exchange_rate)
                soup = BeautifulSoup(prices[i], 'html.parser')
                soup.contents[0].replace_with(format(vnd_value))
                format_price = str(soup)
                prices[i] = "{:,.0f}₫".format(float(format_price) * 1).replace(',', '.')
            if(char_deleted_for_prices in prices[i]):
                prices[i] = prices[i].replace(char_deleted_for_prices, '')


    if (sizes != None):
        for i in range(len(sizes)):
            result = re.search('\(([^)]+)', sizes[i]).group(1)
            sizes[i] = result
    


    for i in range(len(locations2)):
        try:
            if(sizes[i] == ''):
                sizes[i] = 'None'
        except IndexError:
            sizes.append('None')

        if i >= len(sizes):
            sizes.append('None')
        else:
            if sizes[i] == '':
                sizes[i] = 'None'

        try:
            if(prices[i] == ''):
                prices[i] = 'Price on application'
        except IndexError:
            prices.append('Price on application')

        if i >= len(prices):
            prices.append('Price on application')
        else:
            if prices[i] == '':
                prices[i] = 'Price on application'

        try:
            if(property_attribute_values[i] == ''):
                property_attribute_values[i] = 'Attribute values on application'
        except IndexError:
            property_attribute_values.append('Attribute values on application')

        if i >= len(property_attribute_values):
            property_attribute_values.append('Attribute values on application')
        else:
            if property_attribute_values[i] == '':
                property_attribute_values[i] = 'Attribute values on application'

        item =  {
            "price": prices[i],
            "size": sizes[i],
            "attribute": property_attribute_values[i],
            "locations": locations1[i],        
            "location2": locations2[i]
        }
        list_properties_info.append(item)
    
    

    json_data = json.dumps(list_properties_info)
    print(prices)
    print("============================================================")
    print(link_index)
    print("============================================================")

#Xóa các data không cần thiết trước khi lưu vào file json
for i in list_properties_info: 
        if (i['price'] == 'Price on application'): 
            list_properties_info.pop(list_properties_info.index(i))

with open('temp_data.json', 'w', encoding='utf-8') as outfile:
    json.dump(list_properties_info, outfile, ensure_ascii=False)
