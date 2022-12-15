from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    """
    Class for user object creation.
    Uses default django forms module.
    """
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    username = forms.CharField(max_length=30, required=True, help_text='Required')
    
    class Meta:
        """
        Class providing fields labels for form
        """
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2', )