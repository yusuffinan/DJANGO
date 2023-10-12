from . import views
from django.urls import path



urlpatterns = [
    path('',views.index, name="index"),
    path("search",views.search, name="search"),
    path('course-create',views.course_create, name="course_create"),
    path('<slug:slug>', views.details, name="course_details"),
    path("kategori/<slug:slug>", views.getCoursesByCategory, name="courses_by"),
]

