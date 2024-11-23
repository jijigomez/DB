from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, SignupForm
from .models import UserProfile
from django.contrib.auth.models import User

def login_page(request):
    if request.user.is_authenticated:
        return redirect('search_page')  # Replace with your search page's URL name

    messages.info(request, 'Please login to access your account.')

    if request.method == 'POST':       
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('search_page')
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
        else:
            messages.error(request, 'Invalid form submission. Please check your input.')
    else:
        form = LoginForm()

    return render(request, 'login_page.html', {'form': form})

def register_page(request):
    if request.user.is_authenticated:
        return redirect('search_page')

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user_type = form.cleaned_data['type']
            
            user = User.objects.create_user(username=username, email=email, password=password)
            UserProfile.objects.create(user=user, type=user_type)

            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login_page')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SignupForm()

    return render(request, 'register_page.html', {'form': form})

def logout_page(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('login_page')
