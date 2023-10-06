from datetime import date
from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import course, Category

data = {
    'programlama':'programlama kurs listesi',
    'web':'web listesii',
    'mobil': 'mobil uygulamalar'

}
db = {
    'courses' : [
        {
            "title" : "javascript kursu",
            "description" : "javascript kursunun açıklaması burada",
            "imageUrl": "j.png",
            "slug": "javascript-kursu",
            "date": date(2023,2,10),
            "isActive": True,
            "isUpdate" : True
        },
        {
            "title" : "web kursu",
            "description" : "web kursunun açıklaması burada",
            "imageUrl": "h.png",
            "slug": "web-kursu",
            "date": date(2023,2,11),
            "isActive": True,
            "isUpdate" : True
        },
        {
            "title" : "Python kursu",
            "description" : "Python kursunun açıklaması burada",
            "imageUrl": "p.png",
            "slug": "Python-kursu",
            "date": date(2023,2,12),
            "isActive": True,
            "isUpdate" : True
        }
    ],
    'categories': [
        {"id": 1, "name" : "programlama", "slug" :"programlama"},
        {"id": 2, "name" : "web gelistirme", "slug" :"web-gelistirme"},
        {"id": 3, "name" : "mobil uygulamalar", "slug" :"mobil-uygulamalar"},
        ]
}


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
def getCoursesByCategory(request,category_st):
    try:
        text = data[category_st]
        return render(request, 'courses/kurslar.html', {
            'category': category_st,
            'category_text': text
        })
    except:
        text ="yanlış girinti"
        return HttpResponseNotFound("yanlış kategori seçimi")
def getCoursesByCategoryid(request, category_id):
    category_list = list(data.keys())
    if category_id > len(category_list):
        return HttpResponseNotFound("yanlış kategori")
    redirect_t = category_list[category_id  - 1]
    redirect_url = reverse('courses_by', args=[redirect_t])
    return redirect(redirect_url)