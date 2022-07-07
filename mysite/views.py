from django.shortcuts import render
from mysite.models import News
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
