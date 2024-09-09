from django.shortcuts import render,redirect
from django.http import HttpResponse
from .form import Custom_User_form
from django.contrib.auth.models import User
#from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def my_view(request):
    return HttpResponse("Hello, world!")


def signup(request):
    if request.method =="POST":
        form = Custom_User_form(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            if User.objects.filter(email = email).exists():
                messages.error("The email has been taken already")
                return redirect('/')
            else:
                User.objects.create_user(email=email, password=password)
                messages.success(request, "Account created successfully! Please log in.")
    else:
        form = Custom_User_form()
    
    return render(request,'signup.html',{'form': form})









def login(request):
    pass
    #return render(request,'login.html')
