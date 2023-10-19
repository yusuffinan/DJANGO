from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def user_login(request):
    if request.user.is_authenticated and "next" in request.GET:
           return render(request, "account/login.html",{"error":"Yetkiniz yok"})
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get("next", None)
            if next_url is None:
                return redirect("index")
            else:
                return redirect(next_url)
            
        else:
            return render(request, "account/login.html",{"error":"Hatalı bili girdiniz"})
    else:
        return render(request, "account/login.html")

def user_register(request):
    if request.method=="POST":
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        repassword=request.POST["repassword"]

        if repassword != password:
            return render(request,"account/register.html",{
                "error":"Şifreler uyuşmuyor.",
                "username": username,
                "email":email
            })
        if User.objects.filter(username=username).exists():
            return render(request,"account/register.html",{
                "error":"Bu kullanıcı adı zaten alınmış.",
                "username": username,
                "email":email
                })
        if User.objects.filter(email=email).exists():
            return render(request,"account/register.html",{
                "error":"Bu email zaten alınmış.",
                "username": username,
                "email":email
                
                })
        
        user = User.objects.create_user(username=username, password=password, email= email)
        user.save()
        return redirect("user_login")
    else:
        return render(request,"account/register.html")
def user_logout(requst):
    logout(requst)
    return redirect("user_login")
