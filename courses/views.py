from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def kurslar(request):
    return HttpResponse('kurs listesi')
def details(request):
    return HttpResponse('Detaylar')
def programlama(request):
    return HttpResponse('Programalama')
def mobiluygulamalar(request):
    return HttpResponse('Mobil uygulama')
def getCoursesByCategory(request,category):
    text = ""
    if category == "program":
        text = "program kurs"
    elif category == "web":
        text = "web kurslar"
    else:
        text = "yanllış girinti"
    return HttpResponse(text)