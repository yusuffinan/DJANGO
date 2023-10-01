from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

data = {
    'programlama':'programlama kurs listesi',
    'web':'web listesii',
    'mobil': 'mobil uygulamalar'

}


def index(request):
   cateveri = list(data.keys())
   return render(request, 'courses/index.html', {
       'categories': cateveri
   })
   


def details(request,kurs_adi):
    return HttpResponse(f'{kurs_adi} kursu')
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