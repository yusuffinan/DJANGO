from datetime import date
from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import course, Category
from django.core.paginator import Paginator

def index(request):
   kurslar = course.objects.filter(isActive=1)
   kategoriler = Category.objects.all()
   return render(request, 'courses/index.html', {
       'categories' : kategoriler,
       'courses' : kurslar
   })
   


def details(request,slug):
    try:
        Course = course.objects.get(slug=slug)
    except:
        raise Http404("yanlis")
    context ={
        'Course' : Course
    }
    return render(request, 'courses/details.html', context)
def programlama(request):
    return HttpResponse('Programalama')
def mobiluygulamalar(request):
    return HttpResponse('Mobil uygulama')
def getCoursesByCategory(request,slug):
        kurslar = course.objects.filter(categories__slug=slug, isActive=True).order_by("date")
        kategoriler = Category.objects.all()

        paginator = Paginator(kurslar, 2)
        page = request.GET.get('page', 1)
        page_obj = paginator.page(page)
        
        return render(request, 'courses/index.html', {
        'categories' : kategoriler,
        'courses' : page_obj,
        'selected_category' : slug
        })
    
