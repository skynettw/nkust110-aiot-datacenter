from django.contrib import admin
from django.urls import path
from mysite import views

urlpatterns = [
    path('jquery-test/', views.jquery_test),
    path('mongodb-test/', views.mongodb_test),
    path('api/mongodb/<str:keyword>/', views.api_mongodb),
    path('api/stock/<str:code>/', views.api_stock),
    path('chart/', views.chart),
    path('show/<int:id>/', views.show),
    path('company/<int:id>/', views.company),
    path('stockinfo/', views.stockinfo),
    path('stockinfo/<int:id>/', views.stockinfo),
    path('stock/', views.stock),
    path('lotto/', views.lotto),
    path('', views.index),
    path('admin/', admin.site.urls),
]
