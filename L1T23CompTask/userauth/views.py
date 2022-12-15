from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from .forms import SignUpForm

def user_login(request):
    """
    This function calls inbuilt render function
    requests and renders the login html with the 
    authentication folder.
    """
    return render(request, 'authentication/login.html')

def authenticate_user(request):
    """
    This function uses Django's built in authentication
    functionality to authenticate the user name and 
    and password from the database user object.
    If authentication fails, redirect back to login page.
    If successful, redirect to home page. 

    :param request: request username and password

    :rtype: re-request login info if none, else redirect to home page
    """
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
        reverse('userauth:login')
    )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('personalbio:home')
    )

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('userauth:login')
    else:
        form = SignUpForm()
    return render(request, 'authentication/signup.html', {'form': form})