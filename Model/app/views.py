#!/usr/bin/env python
#*-* coding:utf-8 *-*
from django.shortcuts import render
from django.http import HttpResponse

from . import models as m

def index(request):
    articles = m.Artigo.objects.all()
    return render(request, 'list.html', {'articles':articles})

def insert(request,**kwds):
    aut = m.Autor(nome='Brumazzi',email='brumazzi_daniel@yahoo.com.br')
    age = m.Agencia(nome='BCorp',site='pagina.com.br')
    aut.save()
    age.save()
    return HttpResponse('Cadastrado!')
    #art = m.Artigo()
