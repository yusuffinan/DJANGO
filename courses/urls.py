from . import views
from django.urls import path



urlpatterns = [
    path('list',views.kurslar),
    path('details', views.details),
    path('programlama', views.programlama),
    path('mobil-uygulamalar',views.mobiluygulamalar),
    path("<category>", views.getCoursesByCategory),
]

