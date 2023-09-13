from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
# Create your views here.
# def login_render(request):
  # pass


def login(request):
  if request.method == 'POST':
    # print('Login Successful')
    username = request.POST['userId_login']
    password = request.POST['password_login']
    # print('login triggered')
  return render(request, 'registration/login.html')


def sign_up(request):
  if request.method == 'POST':
    # print('Sign In Successful')
    print(request.POST)
    username = request.POST['userId_signup']
    email = request.POST['email_signup']
    password = request.POST['password_signup']
    repassword = request.POST['rePassword_signup']
    
    
    if password == repassword:
      user = User.objects.create_user(username, email, password)
      user.save()
      return redirect('dashboard/home/')
    else:
      pass

    
  return render(request, 'registration/login.html')