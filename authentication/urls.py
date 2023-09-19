from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns =[
    path('', views.login_block),
    path(r'login/', views.login_block, name = 'signin'),
    path(r'sign_up/', views.sign_up),
    
]


