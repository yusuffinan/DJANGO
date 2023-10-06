from . import views
from django.urls import path



urlpatterns = [
    path('',views.index),
    path('<slug:slug>', views.details, name="course_details"),
    path("kategori/<int:category_id>", views.getCoursesByCategoryid),
    path("kategori/<str:category_st>", views.getCoursesByCategory, name="courses_by"),
]

