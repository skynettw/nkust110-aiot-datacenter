from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pdate = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    class Meta:
        ordering = ('-pdate',)
    def __str__(self):
        return self.title

class CompanyType(models.Model):
    name = models.CharField(max_length=50, default="其他", verbose_name="類別")
    def __str__(self):
        return self.name

#預設值只有在資料表中已有記錄的情況下才能夠使用，如果是全新的資料表，就不要使用這個函式
def get_default_ct():
    return CompanyType.objects.get(id=1).id

class Company(models.Model):
    ct = models.ForeignKey(CompanyType, default=get_default_ct, 
                           on_delete=models.CASCADE, verbose_name="類別")
    code = models.CharField(max_length=10, verbose_name="編碼")
    name = models.CharField(max_length=20, verbose_name="名稱")
    def __str__(self):
        return "({},{})".format(self.name, self.code)
    
class StockInfo(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="公司名稱")
    dateinfo = models.DateField(verbose_name="日期")
    open_price = models.FloatField(verbose_name="開盤價")
    close_price = models.FloatField(verbose_name="收盤價")
    volume = models.PositiveIntegerField(verbose_name="成交量")
    def __str__(self):
        return "({},{},{})".format(self.company, self.dateinfo, self.close_price)
    