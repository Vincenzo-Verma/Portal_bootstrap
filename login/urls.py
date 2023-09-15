from django.urls import path
from . import views

urlpatterns =[
    path('', views.login_block),
    path('login/', views.login_block),
    path('sign_up/', views.sign_up),
    
]


