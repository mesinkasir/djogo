from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from contact.models import Contact
def index(request):
    return render(request, "contact/index.html",{
        "contact":Contact.objects.all()
    })
    

