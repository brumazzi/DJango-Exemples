from django.shortcuts import render

from .models import Image
from .forms import ImageForm

def index(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            iname = form.cleaned_data['name']
            img = Image(name=iname, file=request.FILES['file'])
            img.save()
    return render(request,'index.html',{'form':ImageForm()})
