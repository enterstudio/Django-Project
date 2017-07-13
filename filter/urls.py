from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^search\D+$', views.search, name='search'),
    url(r'^', views.index, name='filter'),
    ]