from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
# Create your views here.

data = {
    'programlama':'programlama kurs listesi',
    'web':'web listesii'

}
def kurslar(request):
    return HttpResponse('kurs listesi')
def details(request,kurs_adi):
    return HttpResponse(f'{kurs_adi} kursu')
def programlama(request):
    return HttpResponse('Programalama')
def mobiluygulamalar(request):
    return HttpResponse('Mobil uygulama')
def getCoursesByCategory(request,category_st):
    try:
        text = data[category_st]
    except:
        text ="yanlış girinti"
    return HttpResponse(text)
def getCoursesByCategoryid(request, category_id):
    category_list = list(data.keys())
    if category_id > len(category_list):
        return HttpResponseNotFound("yanlış kategori")
    redirect_t = category_list[category_id  - 1]
    return redirect('/kurs/kategori/' + redirect_t )