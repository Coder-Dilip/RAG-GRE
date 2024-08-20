from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('home/',views.home),
    path('save-vocab/', views.save_vocab, name='save_vocab'),

]
