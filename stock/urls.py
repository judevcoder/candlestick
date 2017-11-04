from django.conf.urls import url
from django.contrib import admin
from stock import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^stock_data', views.stockdata, name='stockdata'),
]