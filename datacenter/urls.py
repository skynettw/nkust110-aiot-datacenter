from django.contrib import admin
from django.urls import path
from mysite import views

urlpatterns = [
    path('show/<int:id>/', views.show),
    path('lotto/', views.lotto),
    path('', views.index),
    path('admin/', admin.site.urls),
]
