from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import*


# Create your views here.
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def services(request):
    return render(request,"services.html")
def resume(request):
    return render(request,"resume.html")
def contact(request):
    return render(request,"contact.html")