from django.shortcuts import render
from . models import*
# Create your views here.

def home(request):
    return render(request,'core/index.html')


def project(request):
    project = Project.objects.all()
    return render(request,'core/project.html',{'project':project})