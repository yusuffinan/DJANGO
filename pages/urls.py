from . import views
from django.urls import path

urlpatterns = [
    path('',views.index),
    path('index',views.index),
    path('contact', views.contact),
    path('about', views.about),
]

