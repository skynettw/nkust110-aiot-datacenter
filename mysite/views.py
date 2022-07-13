from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from mysite.models import News, Company, CompanyType, StockInfo
import random
from plotly.offline import plot
import plotly.graph_objs as go

def index(request):
    if request.method=="POST":
        keyword = request.POST.get("keyword")
        news = News.objects.filter(content__contains=keyword)
    else:
        news = News.objects.all()
    count = len(news)
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

def stockinfo(request, id=1):
    if request.method=="POST":   #如果是使用表單轉來這個網頁的
        comp = request.POST.get("comp")
        company = Company.objects.get(id=comp)
    else:                        #如果不是使用表單轉來這個網頁，就直接使用參數id來找出公司
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

def chart(request):
    keywords = ""
    if request.method=="POST":
        keywords = request.POST.get("keywords")
    if keywords == "":
        keywords = "雲科, 北科, 高科"
    keywords = keywords.split(",")
    data = list()
    for keyword in keywords:
        data.append(News.objects.filter(content__contains=keyword.strip()).count())
    
    return render(request, "chart.html", locals())

def jquery_test(request):

    return render(request, "jquery-test.html", locals())

def api_stock(request, code):
    try:
        c = Company.objects.get(code=code)
        data = StockInfo.objects.filter(company=c)
        stock_data = [(d.dateinfo.strftime("%Y-%m-%d"), d.close_price, d.volume) for d in data]
        return JsonResponse({"status":"ok", "data":stock_data})
    except:
        return JsonResponse({"status":"fail"})
