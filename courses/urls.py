from . import views
from django.urls import path



urlpatterns = [
    path('',views.index),
    path('<slug:slug>', views.details, name="course_details"),
    path("kategori/<slug:slug>", views.getCoursesByCategory, name="courses_by"),
]

