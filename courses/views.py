from django.shortcuts import get_object_or_404, render,redirect
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from courses.forms import CategoryCreate, CourseCreateForm, CourseEditForm, UploadForm
from .models import UploadModel, course, Category
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, user_passes_test

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
    
def isAdmin(user):
     return user.is_superuser

@user_passes_test(isAdmin)
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

@user_passes_test(isAdmin)
def course_create(request):
    if request.method=="POST":
          form = CourseCreateForm(request.POST, request.FILES)
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


@user_passes_test(isAdmin)
def course_edit(request, id):
     coursed = get_object_or_404(course, pk=id) 
     if request.method == "POST":
          form = CourseEditForm(request.POST, request.FILES, instance=coursed)
          form.save()
          return redirect("course_list")
     else:
        form = CourseEditForm(instance=coursed)
     return render(request, 'courses/edit-course.html', { "form":form } )

@user_passes_test(isAdmin)
def course_delete(request, id):
     coursed = get_object_or_404(course, pk=id)
     if request.method == "POST":
          coursed.delete()
          return redirect("course_list")
     return render(request, 'courses/course-delete.html', {"coursed":coursed})

def upload(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
             model = UploadModel(image=request.FILES["imagey"])
             model.save()
             return render(request,"courses/success.html")
    else:
         form = UploadForm()
         return render(request,"courses/upload.html", {"form":form})


  

def details(request,slug):
    try:
        Course = course.objects.get(slug=slug)
    except:
        raise Http404("yanlis")
    kayitli_mi = Course.kullanicilar.filter(id=request.user.id).exists()
    context ={
        'Course' : Course,
        'kayitli_mi' : kayitli_mi,
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

@login_required
def register_for_course(request, id):
    if request.method == "POST":
        ku = get_object_or_404(course, pk=id)
        request.user.kurslar.add(ku)
        return redirect("index")
    else:
        return render(request, 'courses/details.html')   