import http.client, urllib.parse
import json

conn = http.client.HTTPConnection('api.positionstack.com')

params = urllib.parse.urlencode({
    'access_key': 'b35ed365b02974824db234fa58a62426',
    'query': 'Diamond Island, Binh Trung Tay, District 2, Ho Chi Minh City, Vietnam',
    'limit': 1,
    })

conn.request('GET', '/v1/forward?' + params)

res = conn.getresponse()
data = res.read()

# print(data.decode('utf-8'))

json_data = json.loads(data.decode("utf-8"))
latitude = json_data["data"][0]["latitude"]
longitude = json_data["data"][0]["longitude"]

print(f"Latitude: {latitude}, Longitude: {longitude}")
#https://positionstack.com/usage