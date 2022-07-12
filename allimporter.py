import requests
from datetime import datetime
import json, time
import django, os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datacenter.settings')
django.setup()

from mysite.models import Company, StockInfo

target = ['1101', '1102']
url = "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20220{}01&stockNo={}"
urls = list()
for c in target:
    for i in range(1, 8):
        temp_dict = dict()
        temp_dict['code'] = c
        temp_dict['url'] = url.format(i, c)
        urls.append(temp_dict)
for u in urls:
    print(u)
    try:
        data = json.loads(requests.get(u['url']).text)
        c = Company.objects.get(code=u['code'])
        stock_data = data['data']
        for s in stock_data:
            yy, mm, dd = s[0].split("/")
            the_date = datetime(int(yy)+1911, int(mm), int(dd))
            rec = StockInfo.objects.filter(company=c, dateinfo=the_date)
            if len(rec)==0:
                rec = StockInfo(company=c, dateinfo=the_date, 
                                open_price=float(s[3].replace(",", "")), 
                                close_price=float(s[6].replace(",", "")), 
                                volume = int(s[8].replace(",", "")))
                rec.save()
                print(rec.company, rec.close_price)
    except Exception as e:
        print(e)
    time.sleep(5)