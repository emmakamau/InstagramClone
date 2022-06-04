from django.urls import path
from . import views

urlpatterns=[
    path('',views.homepage,name='homepage'),
    path('login/',views.loginuser,name='login'),
    path('signup/',views.signup,name='signup')
]