from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from account.forms import LoginUserForm, NewUserForm

def user_login(request):
    if request.user.is_authenticated and "next" in request.GET:
           return render(request, "account/login.html",{"error":"Yetkiniz yok"})
    
    if request.method=="POST":
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.add_message(request,messages.SUCCESS, "Giriş başarılı.")
                next_url = request.GET.get("next", None)
                if next_url is None:
                    return redirect("index")
                else:
                    return redirect(next_url)
            else:
                return render(request, "account/login.html", {"form":form}) 
            
        else:
            return render(request, "account/login.html", {"form":form})
    else:
        form = LoginUserForm()
        return render(request, "account/login.html", {"form": form})

def user_register(request):
    if request.method=="POST":
       form = NewUserForm(request.POST)

       if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect("index")
       else:
           return render(request, "account/register.html", {"form":form})
    else:
        form = NewUserForm()
        return render(request, "account/register.html", {"form":form})
def user_logout(requst):
    logout(requst)
    messages.add_message(requst,messages.ERROR,"Çıkış yapıldı")
    return redirect("user_login")
