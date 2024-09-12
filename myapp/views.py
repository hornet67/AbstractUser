from django.shortcuts import render,redirect
from myapp.form import *
from django.contrib.auth import get_user_model
from django.contrib import messages
# from .models import CustomUser



def signup(request):
    User = get_user_model()
    if request.method =="POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            if User.objects.filter(email = email).exists():
                messages.error("The email has been taken already")
                return redirect('signup')
            else:
                User.objects.create_user(email=email, password=password)
               
                messages.success(request, "Account created successfully! Please log in.")
                return redirect('login')

    form = CustomUserForm()
    
    return render(request,'signup.html',{'form': form})


def signin(request):
    return render(request,'login.html')
