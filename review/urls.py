
from django.contrib import admin
from django.urls import path
from . import views



app_name = "polls"

urlpatterns = [
     path('', views.home, name="home"),
     path('index/', views.index, name="index"),

     ]