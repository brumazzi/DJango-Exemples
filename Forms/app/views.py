#*-* coding:utf-8 *-*

from django.shortcuts import render
from django.http import HttpResponse
from app.models import Pessoa
from app.forms import FormPessoa

def index(request,*args,**kwds): # O formulário só funciona em GET
    every = Pessoa.objects.all()
    f = FormPessoa()
    if 'nome' in request.GET:
        name = request.GET['nome']
        nasci = request.GET['nascimento']
        descr = request.GET['descri']
        p = Pessoa()
        p.nome = name
        p.nasci = nasci
        p.descr = descr
        p.save()
    return render(request,'index.html',{'person':every,'form':f.as_table()})

def form_action(request):
    if 'nome' in request.GET:
        name = request.GET['nome']
        nasci = request.GET['nascimento']
        descr = request.GET['descri']
        p = Pessoa()
        p.nome = name
        p.nasci = nasci
        p.descr = descr
        p.save()
        return HttpResponse('Cadastrado com sucesso!')

    return HttpResponse("Erro ao efetuar o cadastro.")
