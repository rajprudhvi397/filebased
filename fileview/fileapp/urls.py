from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

urlpatterns=[
    path('',cache_page(40)(views.home)),
    path('home', views.home),
    path('about',views.about),
]