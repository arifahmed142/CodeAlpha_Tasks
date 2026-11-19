from django.urls import path
from . import views

urlpatterns = [
    path('Login/', views.login, name='Login'),
    path('Logout/', views.auth_logout, name='Logout'),
    path('Register/', views.register, name='Register'),
    path('Profile/',views.profile, name='Profile')
]