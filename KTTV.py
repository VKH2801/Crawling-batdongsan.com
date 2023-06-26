import requests
import bs4

URL = "https://www.nchmf.gov.vn/kttv/"

html = requests.get(URL).text
document = bs4.BeautifulSoup(html, 'html.parser')

target = document.select(".wt-city")
target = target[0]
target = target.findAll("li")

result = {}
for entry in target:
    result[entry.find("a").getText()] = entry.findAll("div")[1].getText()

print(result)