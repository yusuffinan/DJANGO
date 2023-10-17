from . import views
from django.urls import path



urlpatterns = [
    path('',views.index, name="index"),
    path("search",views.search, name="search"),
    path("category-create",views.category_create, name="category_create"),
    path("category-list", views.category_list, name="category_list"),
    path('course-create',views.course_create, name="course_create"),
    path("course-list", views.course_list, name="course_list"),
    path("course-edit/<int:id>",views.course_edit, name="course_edit"),
    path("course-delete/<int:id>",views.course_delete, name="course_delete"),
    path("upload", views.upload, name="upload_image"),
    path('<slug:slug>', views.details, name="course_details"),
    path("kategori/<slug:slug>", views.getCoursesByCategory, name="courses_by"),
]

