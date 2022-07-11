from django.contrib import admin
from mysite.models import News, Company, StockInfo, CompanyType

admin.site.register(News)
admin.site.register(Company)
admin.site.register(StockInfo)
admin.site.register(CompanyType)