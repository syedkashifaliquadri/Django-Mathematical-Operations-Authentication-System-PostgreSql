from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('exp',views.exp, name='exp'),
    path('plus',views.plus,name='plus'),
    path('minus',views.minus,name='minus'),
]