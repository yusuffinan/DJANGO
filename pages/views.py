from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.

def index(request):
    return redirect("index")
def about(request):
    return render(request,"pages/about.html")
def contact(request):
    return render(request,"pages/contact.html")