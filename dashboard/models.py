from django.db import models

# Create your models here.
class User(models.Model):
  GENDER_CHOICES = [
  ('M', 'Male'),
  ('F', 'Female'),
  ('O', 'Others'),
  ]
  uname = models.CharField(max_length = 255, primary_key = True)
  f_name = models.CharField(max_length = 255)
  l_name = models.CharField(max_length = 255)
  fatherName = models.CharField(max_length = 255)
  motherName = models.CharField(max_length = 255)
  dob = models.DateField()
  institutuionName= models.CharField(max_length = 255)
  gender = models.CharField(max_length = 1, choices = GENDER_CHOICES)
  phoneNumber = models.CharField(max_length = 255)
  email = models.EmailField(unique = True)
  address = models.TextField()

class FormStatus(models.Model):
  # formId = models.AutoField
  DOCUMENT_STATUS_UNVERIFIED = 'F'
  DOCUMENT_STATUS_VERIFIED = 'T'
  DOCUMENT_STATUS_PENDING = 'P'
  DOCUMENT_STATUS_CHOICES = [
   (DOCUMENT_STATUS_UNVERIFIED, 'Unverified'),
   (DOCUMENT_STATUS_VERIFIED, 'Verified'),
   (DOCUMENT_STATUS_PENDING, 'Pending'),
  ]
  status = models.CharField(max_length = 1, choices = DOCUMENT_STATUS_CHOICES, default = DOCUMENT_STATUS_UNVERIFIED)
  lastUpdate =  models.DateField(auto_now = True)
  User = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)

class BankDatails(models.Model):
  accountNumber = models.CharField(max_length = 255)
  bankName =  models.CharField(max_length = 255)
  bankIfsc = models.CharField(max_length = 255)
  User =  models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
