from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import *
from .forms import *
from django.contrib.auth import authenticate, login, logout

# Create your views here.
# @unauthenticated_user
def signup(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()

            messages.success(request, "Account created successfully")
            return redirect('login')

    context = {
        'form': form,
    }
    return render (request, 'accounts/signup.html', context=context)

#@unauthenticated_user
def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.info(request, "Username or Password is incorrect")
            
    context = {}
    return render (request, 'accounts/login.html', context=context)

def logoutuser(request):

    logout(request)
    return redirect('login')

#@login_required(login_url='login')
def homepage(request):

    context={}
    return render(request,'index.html',context=context)

#@login_required(login_url='login')
def profile(request,username):
    user_name = User.objects.get(username=username)
    user_profile = Profile.objects.get(user=user_name.id)

    user_posts = Post.objects.filter(image_owner=user_name.id)
    post_comments = Comment.objects.all()
    # for post in user_posts:
    #     post_comments = Comment.objects.filter(post_associated=post.id)
    #     print(post_comments)
    
    context={
        'user_name':user_name,
        'user_profile':user_profile,
        'user_posts':user_posts,
        'post_comments':post_comments
    }
    return render(request,'profile.html',context=context)