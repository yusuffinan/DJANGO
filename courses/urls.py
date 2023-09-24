from . import views
from django.urls import path



urlpatterns = [
    path('',views.home),
    path('anasayfa',views.home),
    path('kurslar',views.kurslar),
]

