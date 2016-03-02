#!/usr/bin/env python
#*-* coding:utf-8 *-*
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request, offset):
    out = ""

    if offset is not None:
        out = "Parametro atual: %s" %(offset)
    else:
        out = "Sem parametro"

    return HttpResponse(out)

def home(request):
    return HttpResponse("Pagina inicial")
