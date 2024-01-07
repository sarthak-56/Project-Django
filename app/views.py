from django.shortcuts import render, redirect ,HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Customer

def home(request):
    return render(request, 'home.html')

def main(request):
    return render(request,'main.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        emailid = request.POST['emailid']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        # Add any additional fields as needed
        if password != confirmpassword:
            return HttpResponse("password not match")
        else:

        # Create a new user
            user = User.objects.create_user(username=username, password=password)
            # You may want to log in the user after signup
            login(request, user)
            return redirect('login')

    return render(request, 'signup.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            # Handle invalid login
            pass

    return render(request, 'login.html')


    