#匯入所有上市公司的類別資料
url = "https://isin.twse.com.tw/isin/C_public.jsp?strMode=2"
import requests
from bs4 import BeautifulSoup
import django, os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datacenter.settings')
django.setup()

from mysite.models import CompanyType
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")
rows = soup.find_all("tr")
for i, row in enumerate(rows):
    if i>=2:
        try:
            cells = row.find_all("td")
            if cells[0].text[0] == "0":
                break
            code, name, ct = cells[0].text.split("　")[0], cells[0].text.split("　")[1], cells[4].text
            print(code, name, ct)
            rec = CompanyType.objects.filter(name=ct.strip())
            if len(rec)==0:
                rec = CompanyType(name=ct.strip())
                rec.save()
        except:
            pass