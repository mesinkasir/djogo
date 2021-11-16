from django.shortcuts import render
from django.http import HttpResponse

from home.models import Home

# Create your views here.

def index(request):
    return render(request,"home/index.html",{
        "home":Home.objects.all()
    })