from django.shortcuts import render

menu = ['Home','Help','Contact']

def index(request):
    #print request
    return render(request, 'index.html', {'menu_items' : menu})
