from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('home/', views.home, name = 'home' ),
    path('first_page/', views.first_page, name = 'first_page'),
    path('logout_user/', views.logout_user, name = 'logout_user')
]