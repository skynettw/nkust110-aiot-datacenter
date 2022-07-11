import requests
import json
target = ['2303', '2344', '2337']
url = "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20220{}01&stockNo={}"
urls = list()
for c in target:
    for i in range(1, 8):
        urls.append(url.format(i, c))
for u in urls[:1]:
    data = json.loads(requests.get(u).text)
    print(data)
