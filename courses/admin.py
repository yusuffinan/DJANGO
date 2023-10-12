from django.contrib import admin
from .models import course,Category

@admin.register(course)
class courseAdmin(admin.ModelAdmin):
    list_display = ("title", "isActive","isHome", "slug","category_list",)
    prepopulated_fields = {"slug": ("title",),}
    list_filter = ("title", "isActive","isHome",)
    list_editable = ("isActive", "isHome",)
    search_fields = ("title", "description",)
    def category_list(self, obj):
        html=""
        for categoryy in obj.categories.all():
            html += categoryy.name + ""
        return html


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","slug","course_list",)
    prepopulated_fields = {"slug": ("name",),}
    def course_list(self, obj):
         return obj.course_set.count()
