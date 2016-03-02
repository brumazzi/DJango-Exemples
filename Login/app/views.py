from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.conf import settings

def index(request):
    if request.user.is_authenticated():
        return render(request,'login.html',{'login':True})
    if 'f' in request.GET:
        if request.GET['f'] == 'register':
            register(request)
            return redirect('index')
    if request.method == "POST":
        log = request.POST['log']
        pas = request.POST['pass']

        auth = authenticate(username=log,password=pas)
        if auth is not None:
            if auth.is_active:
                login(request,auth)
                return redirect('index')
                #return render(request,'login.html',{'login':True})
            else:
                return render(request,'login.html',{'err':"Not possible login with this user."})
        else:
            return render(request,'login.html',{'err':'Login or pass invalids!'})
    
    return render(request,'login.html')

def register(request):
    if request.user.is_authenticated():
        return redirect('home')
    if request.method == 'POST':
        name = request.POST['name']
        lname = request.POST['last_name']
        mail = request.POST['mail']
        passwd = request.POST['pass']
        new = User.objects.create_user(mail,name,passwd)
        new.last_name = lname
        new.save()
        auth = authenticate(username=mail,password=passwd)
        login(request,auth)
        return redirect('home')
    return render(request,'register.html')

        

def logout_view(request): # para que o codigo funcionasse foi necessaria que o metodo tenha esse nome "logout_view"
    if request.user.is_authenticated():
        logout(request)
    return redirect("home")
