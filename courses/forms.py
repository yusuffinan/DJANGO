from django import forms
from django.forms import ModelForm
from courses.models import course

class CourseCreateForm(ModelForm):
    # title = forms.CharField(label="Title", widget=forms.TextInput(attrs={"class":"form-control"}))
    # description = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))
    # imageUrl = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    # slug = forms.SlugField(widget=forms.TextInput(attrs={"class":"form-control"}))
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
