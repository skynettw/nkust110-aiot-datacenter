import pandas as pd
import twstock, datetime
import django, os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datacenter.settings')
django.setup()

from mysite.models import Company, StockInfo
tsmc = twstock.Stock("2330")
data = tsmc.fetch(2022, 6)
df = pd.DataFrame(data)
tsmc_date = list(df.date)
tsmc_open = list(df.open)
tsmc_close = list(df.close)
tsmc_trans = list(df.transaction)
alldata = zip(tsmc_date, tsmc_open, tsmc_close, tsmc_trans)
tsmc_company = Company.objects.get(code="2330")
for d in alldata:
    try:
        rec = StockInfo(
            company = tsmc_company,
            dateinfo = d[0],
            open_price = d[1],
            close_price = d[2],
            volume = d[3]
        )
        rec.save()
    except Exception as e:
        print(e)