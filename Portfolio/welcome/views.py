from os import name
from django.shortcuts import render
from django.http import HttpResponse
from welcome.models import *
from django.http import FileResponse
# Create your views here.


def home(request) :
    return render(request, 'welcome/welcome.html')


def download(request):
    obj = Resume.objects.get(name='shubha')
    filename = obj.resume.path
    response = FileResponse(open(filename, 'rb'))
    return (response)


    