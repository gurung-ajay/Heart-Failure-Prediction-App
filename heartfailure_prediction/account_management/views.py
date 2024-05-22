from django.shortcuts import render, redirect
from . forms import SignUpForm, LoginForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, logout

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('heart_prediction')
            else:
                form.add_error(None, 'Invalid username or password.')
        
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form':form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('heart_prediction')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form':form})


def log_out(request):
    logout(request)
    return redirect('welcome')