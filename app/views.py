from django.shortcuts import render, redirect
from django.contrib import messages
from .decorators import *
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def homepage(request):

    context={}
    return render(request,'index.html',context=context)

@unauthenticated_user
def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Username or Password is incorrect")
            
    context = {}
    return render (request, 'accounts/login.html', context=context)