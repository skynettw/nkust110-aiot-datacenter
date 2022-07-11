from django.contrib import admin
from django.urls import path
from mysite import views

urlpatterns = [
    path('show/<int:id>/', views.show),
    path('company/<int:id>/', views.company),
    path('stockinfo/<int:id>/', views.stockinfo),
    path('stock/', views.stock),
    path('lotto/', views.lotto),
    path('', views.index),
    path('admin/', admin.site.urls),
]
