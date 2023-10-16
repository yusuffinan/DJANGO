from datetime import date
from django.shortcuts import get_object_or_404, render,redirect
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

from courses.forms import CategoryCreate, CourseCreateForm, CourseEditForm
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
    
def category_create(request):
        if request.method=="POST":
          form = CategoryCreate(request.POST)
          if form.is_valid():
                form.save()
                return redirect("/kurs")
        else:
            form = CategoryCreate
        return render(request, "courses/category-create.html", {"form": form})

def category_list(request):
     kategori = Category.objects.all()
     return render(request, 'courses/category-list.html', {
       'categories' : kategori
   })

def course_create(request):
    if request.method=="POST":
          form = CourseCreateForm(request.POST)
          if form.is_valid():
                form.save()
                return redirect("/kurs")
    else:
          form = CourseCreateForm
    return render(request, "courses/course-create.html", {"form": form})

def course_list(request):
     kurslar = course.objects.all()
     return render(request, 'courses/course-list.html', {
       'courses' : kurslar
   })

def course_edit(request, id):
     coursed = get_object_or_404(course, pk=id) 

     if request.method == "POST":
          form = CourseEditForm(request.POST, instance=coursed)
          form.save()
          return redirect("course_list")
     else:
        form = CourseEditForm(instance=coursed)
     return render(request, 'courses/edit-course.html', { "form":form } )

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
    
