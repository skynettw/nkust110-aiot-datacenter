from django.shortcuts import render
import random

def index(request):
    name = "不分系何老師"
    
    lotto = [i for i in range(1,50)]
    random.shuffle(lotto)
    lotto = lotto[:6]
    return render(request, "index.html", locals())
