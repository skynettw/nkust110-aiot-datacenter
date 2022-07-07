from django.contrib import admin
from django.urls import path
from mysite import views

urlpatterns = [
    path('lotto/', views.lotto),
    path('', views.index),
    path('admin/', admin.site.urls),
]
