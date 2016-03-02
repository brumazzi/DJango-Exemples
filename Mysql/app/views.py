from django.shortcuts import render

from app.models import Pessoa, Key

def index(request):
    ap = [{
        'nome':x.name,
        'keys':Key.objects.filter(user=x)
    } for x in Pessoa.objects.all()]
    return render(request,'index.html',{'list':ap})
