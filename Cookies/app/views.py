from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.sessions.backends.db import SessionStore

def index(request):
    if 'x' in request.session.keys() not None:
        request.session['x'] = None
    else:
        request.session['x'] = 'as3213'
    return HttpResponse(request.session['x'])
