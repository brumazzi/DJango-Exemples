#*-* coding: utf-8 *-*
from django.shortcuts import render
from django.http import HttpResponse

import os

def indexof(request):
    files = os.listdir("./indexof/")
    link_list = [{'path':"/download?fpath=%s"%(x),'name':x} for x in files]
    return render(request, "indexof.html", {'link_list':link_list})

def download(request):
    if request.method == "GET":
        print request.GET
        if 'fpath' in request.GET:
            resp = HttpResponse(content_type='application/x-download')
            resp['Content-Disposition'] = "attachment; filename=%s" %(request.GET['fpath'])
            fin = open("indexof/%s" % request.GET['fpath'])
            resp.write(fin.read())
            fin.close()
            return resp
    return HttpResponse("Arquivo para download não selecionado.")

def style(request):
    file = open("app/templates/style.css")
    resp = HttpResponse()
    resp.write(file.read())
    file.close()

    return resp
