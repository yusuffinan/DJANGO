from datetime import date
from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import course, Category
from django.core.paginator import Paginator

def index(request):
   kurslar = course.objects.filter(isActive=1, isHome=1)
   kategoriler = Category.objects.all()
   return render(request, 'courses/index.html', {
       'categories' : kategoriler,
       'courses' : kurslar
   })
   
def search(request):
        if "q" in request.GET and request.GET["q"] != "":
            q = request.GET["q"]
            kurslar = course.objects.filter(isActive=True, title__contains=q).order_by("date")
            kategoriler = Category.objects.all()
        else:
            return redirect("/kurs")

    
        return render(request, 'courses/search.html', {
        'categories' : kategoriler,
        'courses' : kurslar,
        
        })
    

def course_create(request):
     return render(request, "courses/course-create.html")

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
        
        return render(request, 'courses/list.html', {
        'categories' : kategoriler,
        'courses' : page_obj,
        'selected_category' : slug
        })
    
