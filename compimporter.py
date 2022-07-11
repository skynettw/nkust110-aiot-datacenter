#匯入所有上市公司的編碼和名稱
url = "https://isin.twse.com.tw/isin/C_public.jsp?strMode=2"
import requests
from bs4 import BeautifulSoup
import django, os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datacenter.settings')
django.setup()

from mysite.models import CompanyType, Company
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")
rows = soup.find_all("tr")
for i, row in enumerate(rows):
    if i>=2:
        try:
            cells = row.find_all("td")
            if cells[0].text[0] == "0":
                break
            #從網頁中解析出公司的資料（編碼,名稱,類別）
            code, name, ct = cells[0].text.split("　")[0], cells[0].text.split("　")[1], cells[4].text
            print(code, name, ct)
            #取得公司類別在資料表中的記錄
            company_type = CompanyType.objects.get(name=ct.strip())
            rec = Company.objects.filter(name=name.strip())
            if len(rec)==0:
                rec = Company(ct=company_type, code=code.strip(), name=name.strip())
                rec.save()
        except:
            pass