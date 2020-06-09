from django.shortcuts import render
from . import urls

# Create your views here.

def home(request):
    return render(request, 'a.html')

def exp(request):
    a = int(request.GET['text1'])
    b = int(request.GET['text2'])
    c = a * b
    return render(request, 'output.html',{'result':c})

def plus(request):
    a = int(request.GET['text1'])
    b = int(request.GET['text2'])
    c = a + b
    return render(request, 'output.html',{'result':c})

def minus(request):
    a = int(request.GET['text1'])
    b = int(request.GET['text2'])
    c = a - b
    return render(request, 'output.html',{'result':c})
