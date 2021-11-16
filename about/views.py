from django.shortcuts import render
from django.http import HttpResponse

from about.models import About

# Create your views here.

def index(request):
    return render(request,"about/index.html",{
        "about":About.objects.all()
    })