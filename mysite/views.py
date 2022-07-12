from django.shortcuts import render
from mysite.models import News, Company, CompanyType, StockInfo
import random
from plotly.offline import plot
import plotly.graph_objs as go

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

def company(request, id):
    ct = CompanyType.objects.get(id=id)
    companies = Company.objects.filter(ct=ct)
    return render(request, "company.html", locals())

def stockinfo(request, id):
    company = Company.objects.get(id=id)
    data = StockInfo.objects.filter(company=company).order_by('dateinfo')
    last50 = data[:50]
    prices = [d.open_price for d in data]
    volumes = [d.volume/1000 for d in data]
    dates = [d.dateinfo for d in data]
    plot_div = plot(
        [go.Scatter(x=dates, y=prices, mode='lines'), go.Bar(x=dates, y=volumes)], 
        output_type="div")
    return render(request, "stockinfo.html", locals())