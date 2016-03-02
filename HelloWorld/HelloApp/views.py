from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import list_polls

# Create your views here.
def index(request):
    #return HttpResponse("Hell World!")
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'list' : list_polls(),
    })
    return HttpResponse(template.render(context))

def form(request):
    return HttpResponse("Form")
