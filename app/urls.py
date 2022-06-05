from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[
    path('',views.homepage,name='homepage'),
    path('login/',views.loginuser,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logoutuser,name='logout'),

    path('<str:username>/', views.profile, name='profile'),
    path('profile_update/<str:username>/',views.profile_update,name='profile_update'),

    path('<str:username>/delete/<int:post_id>/',views.delete_post,name='delete_post'),
    path('<str:username>/delete/<int:comment_id>/',views.delete_comment,name='delete_comment'),

    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),name="password_reset_complete"),
]