from django.forms import ModelForm, TextInput
from .models import *
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