from django.forms import ModelForm,TextInput
from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['user_comment']
        widgets = {
            'user_comment': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 100%;',
                'placeholder': 'Comment'
                })
            }

class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['prof_pic','bio','website','name']

        def __init__(self, *args, **kwargs):
            super(ProfileUpdateForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()

class PostUpdateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['image_upload','image_name','image_caption']

        def __init__(self, *args, **kwargs):
            super(PostUpdateForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()

        




