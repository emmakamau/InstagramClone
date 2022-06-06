from multiprocessing import context
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import *
from .forms import *
from django.contrib.auth import authenticate, login, logout

from django.views.generic.edit import UpdateView
from django.views.generic import DetailView

# Create your views here.
# @unauthenticated_user
def signup(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            user_profile=Profile(
                user=user,
                name=username
            )
            user_profile.save_profile()

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
    all_posts = Post.objects.all()
    post_comments = Comment.objects.all()

    comment_form = CommentForm()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            post_associated_id = request.POST.get('post_associated')

            user = request.user
            user_profile = Profile.objects.get(user=user.id)
            post_associated = Post.objects.get(id=post_associated_id)
            user_comment = comment_form.cleaned_data['user_comment']

            comment = Comment(
                user=user,
                user_profile=user_profile,
                user_comment=user_comment,
                post_associated=post_associated
                )
            comment.save()
            return redirect('homepage')

    context={
        'all_posts':all_posts,
        'post_comments':post_comments,
        'comment_form':comment_form
    }
    return render(request,'index.html',context=context)

def search_by_username(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        if User.objects.filter(username=user_name):
            return redirect ('profile', username=user_name)
    return render(request,'search.html')

#@login_required(login_url='login')
def profile(request,username):
    user_name = User.objects.get(username=username)
    
    user_profile = Profile.objects.get(user=user_name.id)

    user_posts = Post.objects.filter(image_owner=user_name.id)
    post_comments = Comment.objects.all()

    comment_form = CommentForm()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            post_associated_id = request.POST.get('post_associated')

            user = request.user
            user_profile = Profile.objects.get(user=user.id)
            post_associated = Post.objects.get(id=post_associated_id)
            user_comment = comment_form.cleaned_data['user_comment']

            comment = Comment(
                user=user,
                user_profile=user_profile,
                user_comment=user_comment,
                post_associated=post_associated
                )
            comment.save()
            return redirect('homepage')
    
    context={
        'user_name':user_name,
        'comment_form':comment_form,
        'user_profile':user_profile,
        'user_posts':user_posts,
        'post_comments':post_comments
    }
    return render(request,'profile.html',context=context)

def profile_update(request,username):
    user_name = User.objects.get(username=username)
    user_profile = Profile.objects.get(user=user_name.id)

    data = get_object_or_404(Profile, id=user_profile.id)
    profile_form = ProfileUpdateForm(instance=data)

    if request.method == "POST":
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=data)
        if profile_form.is_valid():
            profile_form.save()
            return redirect ('profile_update', username=user_name)

    context={
        'user_name':user_name,
        'profile_form':profile_form,
        'user_profile':user_profile
    }
    return render(request,'profile_update.html',context=context)

def post_create(request):
    post_create_form = PostCreateForm()

    if request.method == "POST":
        post_create_form = PostCreateForm(request.POST,request.FILES)
        print(post_create_form)
        if post_create_form.is_valid():
            user = request.user
            
            image_upload = post_create_form.cleaned_data.get('image_upload')
            image_name = post_create_form.cleaned_data.get('image_name')
            image_caption  = post_create_form.cleaned_data.get('image_caption')
            image_owner = Profile.objects.get(user=user.id)
            
            new_post = Post(
                image_upload=image_upload,
                image_name=image_name,
                image_caption=image_caption,
                image_owner=image_owner
            )
            new_post.save_post()
            return redirect('homepage')

    context={
        'post_create_form':post_create_form
    }
    return render(request,'post_create.html',context=context)

def post_update(request,username):
    user_name = User.objects.get(username=username)
    user_profile = Profile.objects.get(user=user_name.id)

    data = get_object_or_404(Profile, id=user_profile.id)
    post_update_form = PostUpdateForm(instance=data)

    if request.method == "POST":
        post_update_form = PostUpdateForm(request.POST, instance=data)
        if post_update_form.is_valid():
            post_update_form.save()
            return redirect ('homepage')

    context={
        'user_name':user_name,
        'post_update_form':post_update_form,
        'user_profile':user_profile
    }
    return render(request,'post_update.html',context=context)

def delete_post(request,username,post_id):
    post_to_delete = Post.objects.get(id=post_id)
    post_to_delete.delete_post(post_id)

    return redirect('profile',username=username)

def delete_comment(request,username,comment_id):
    print(comment_id)
    comment_to_delete = Comment.objects.get(id=comment_id)
    comment_to_delete.delete_comment(comment_id)

    return redirect('profile',username=username)

