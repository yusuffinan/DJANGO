from . import views
from django.urls import path



urlpatterns = [
    path('list',views.kurslar),
    path('<kurs_adi>', views.details),
    path("kategori/<int:category_id>", views.getCoursesByCategoryid),
    path("kategori/<str:category_st>", views.getCoursesByCategory),
]

