from django.shortcuts import render
from mysite.models import News, Company, CompanyType, StockInfo
import random

def index(request):
    name = "不分系何老師"
    news = News.objects.all()
    return render(request, "index.html", locals())

def lotto(request):
    lotto = [i for i in range(1,50)]
    random.shuffle(lotto)
    lotto = lotto[:6]
    return render(request, "lotto.html", locals())

def show(request, id):
    item = News.objects.get(id=id)
    return render(request, "show.html", locals())

def stock(request):
    ct = CompanyType.objects.all()
    return render(request, "stock.html", locals())
