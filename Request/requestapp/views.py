from django.shortcuts import render
from django.http import HttpResponse

import datetime

def index(request):
    now = datetime.datetime.now();
    return render(request, 'data.html', {'data_atual' : now})
