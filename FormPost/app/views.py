from django.shortcuts import render
from django.core.mail import send_mail

from app.forms import FormContato

def index(request):
    if request.method == "POST":
        print request.POST
        form = FormContato(request.POST)
        if form.is_valid():
            mail = ['brumazzi_daniel@yahoo.com.br']
            remet = form.cleaned_data['email']
            assun = "CONTATO - %s" %(form.cleaned_data['nome'])
            mess = "Telefone: %s<br/>%s" %(form.cleaned_data['tell'], form.cleaned_data['mess'])
            #send_mail(assun,mess,remet, mail)

            return render(request, "form.html",{"form":FormContato(),"send":True})
    form = FormContato()
    return render(request, "form.html",{"form":form,"send":False})

def index_form(request):
    if request.method == "POST":
        post = [{'input':x,'value':request.POST[x]} for x in request.POST]
    else:
        post = ['--']

    print post

    return render(request,"index.html",{'post':post})
