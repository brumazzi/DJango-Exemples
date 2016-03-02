#!/usr/bin/env python
#*-* coding:utf-8 *-*
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
import datetime

def index(request):
    return HttpResponse("Index")

def date(request, offset):
    try:
        offset = int(offset)
    except error:
        raise Http404();
    date = datetime.datetime.now() + datetime.timedelta(days=offset);
    html = "<em>Em %i dia(s), será %s.</em>" %(offset, date)
    return HttpResponse(html)
