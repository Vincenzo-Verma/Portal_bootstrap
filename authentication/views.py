from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.urls import reverse
# Create your views here.
# def login_render(request):
  # pass


def login_block(request):
  if request.method == 'POST':
    # print('Login Successful')
    username = request.POST.get('userId_login')
    password = request.POST.get('password_login')
    # print('login triggered')
    user = authenticate(username = username, password = password)
    if user is not None:
      print(login(request, user))
      return redirect('dashboard:home')
      # reverse('/dashboard/')
      # redirect('/dashboard/home/')
      # messages.error(request, "User Dosen't exist")
  return render(request, 'registration/login.html')


def sign_up(request):
  if request.method == 'POST':
    # print('Sign In Successful')
    print(request.POST)
    username = request.POST.get('userId_signup')
    email = request.POST.get('email_signup')
    password = request.POST.get('password_signup')
    repassword = request.POST.get('rePassword_signup')
    
    print(username, email, password)
    
    if password == repassword:
      user = User.objects.create_user(username, email, password)
      try:
        print(user.save())
      except:
        messages.error('Username already exists')
      
      login(request, user)
      return redirect('dashboard:home')
    else:
      pass

    
  return render(request, 'registration/login.html')