from django.shortcuts import render
from . import models
# Create your views here.


from django.http import HttpResponse

def index(request):
    return render(request, 'portfolio.html', models.portfolio)

def contact(request):
    return render(request, 'contact.html')

def projects(request):
    return render(request, 'projects.html', models.projects)

def resume(request):
    return render(request, 'resume.html', models.resume)
