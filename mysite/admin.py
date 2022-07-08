from django.contrib import admin
from mysite.models import News, Company, StockInfo

admin.site.register(News)
admin.site.register(Company)
admin.site.register(StockInfo)