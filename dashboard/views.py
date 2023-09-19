from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import User, FormStatus, BankDatails
# Create your views here.
@login_required
def home(request):
  if request.method == 'POST':
    return redirect('dashboard:first_page')
  return render(request, 'home.html')

@login_required
def first_page(request):
  # print('function called')
  print(request.POST)
  if request.method == 'POST':
    f_name = request.POST.get('f_name')
    l_name = request.POST.get('l_name')
    fathername = request.POST.get('fathername')
    mothername = request.POST.get('mothername')
    dob = request.POST.get('dob')
    gender = request.POST.get('gender')
    phonenumber = request.POST.get('phonenumber')
    email = request.POST.get('email')
    address = request.POST.get('address')

    student = User(f_name = f_name, l_name = l_name, fatherName = fathername, motherName = mothername, dob = dob, gender = gender, phoneNumber = phonenumber, email =email, address = address)

    print(student.save())

  return render(request, 'first_page.html')
@login_required
def logout_user(request):
  logout(request)
  return redirect('authentication:signin')


