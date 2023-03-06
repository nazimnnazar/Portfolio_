from django.shortcuts import render

# Create your views here.

def protfolio(request):
    return render(request,'protfolio/protfolio.html')