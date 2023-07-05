from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import json


class WebScraperFacade:
    def __init__(self, base_url, driver_path):
        self.base_url = base_url
        self.driver_path = driver_path
        self.driver = webdriver.Chrome(service = Service(driver_path))

    def scrape_properties(self):
        self.__init__(self.base_url, self.driver_path)
        self._access_base_url()
        self._scrape_property_links()
        self._scrape_property_details()
        self._save_to_json()
        self._close_driver()


    def _access_base_url(self):
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)

    def _scrape_property_links(self):
        list_links_base = []

        for one in range(1, 4):
            list_links_base.append(self.base_url + '/p' + str(one))

        self.list_links_base = list_links_base

    def _scrape_property_details(self):
        list_properties_info = []

        for index in range(len(self.list_links_base)):
            url = self.list_links_base[index]
            self.driver.get(url)
            html_content = self.driver.page_source
            soup = BeautifulSoup(html_content, 'html.parser')

            # Trích xuất thông tin về giá, diện tích, vị trí từ soup
            prices = [i.text for i in soup.find_all('span', {'class' : 're__card-config-price js__card-config-item'})]
            acreages = [i.text for i in soup.find_all('span', {'class' : 're__card-config-area js__card-config-item'})]
            locations = [i.text for i in soup.find_all('div', {'class' : 're__card-location'})]
            char_line_break_to_remove = '\n'
            char_dot_to_remove = '.'
            # Chuẩn hóa dữ liệu
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

                # Tạo đối tượng item và thêm vào list_properties_info
                item = {
                    "price": prices[i],
                    "acreage": acreages[i],        
                    "location": locations[i]
                }
                list_properties_info.append(item)
            print('================================================================')        
            print(url)
            print('================================================================')

        self.list_properties_info = list_properties_info

    def _save_to_json(self):
        with open('Facade_Data.json', 'w', encoding='utf-8') as outfile:
            json.dump(self.list_properties_info, outfile, ensure_ascii=False)

    def _close_driver(self):
        self.driver.quit()


# Sử dụng WebScraperFacade - Tối uwu hơn với chỉ cần 4 dòng code
base_url = 'https://batdongsan.com.vn/nha-dat-ban-tp-hcm'
driver_path = 'path/to/chromedriver'

facade = WebScraperFacade(base_url, driver_path)
facade.scrape_properties()
