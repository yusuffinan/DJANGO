from django import forms
from django.forms import ModelForm
from courses.models import Category, course

class CourseCreateForm(ModelForm):
    class Meta:
        model = course
        fields = ("title", "description", "imageUrl", "slug")
        labels = {
            "title": "Kurs Başlığı",
            "description": "açıklama"
        }
        widgets = {
            "title":forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "imageUrl": forms.TextInput(attrs={"class":"form-control"}),
            "slug": forms.TextInput(attrs={"class":"form-control"})
        }

class CourseEditForm(ModelForm):
    class Meta:
        model = course
        fields = '__all__'
        labels = {
            "title": "Kurs Başlığı",
            "description": "açıklama"
        }
        widgets = {
            "title":forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "imageUrl": forms.TextInput(attrs={"class":"form-control"}),
            "slug": forms.TextInput(attrs={"class":"form-control"})
        }
    
class CategoryCreate(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        labels = {
            "name": "Name",
            "slug": "slug bilgisi"
        }
        widgets = {
            "name":forms.TextInput(attrs={"class": "form-control"}),
            "slug": forms.TextInput(attrs={"class":"form-control"})

        }