from django.shortcuts import render,redirect
from django.contrib.auth.models import auth

# Create your views here.

def login(request):
    if request.method=='POST':
        username1 = request.POST['username']
        password1 = request.POST['password']

        x = auth.authenticate(username=username1,password=password1)

        if x is not None:
            auth.login(request,x)
            return redirect('/')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html')