from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='member_login'),
    path('registration/', views.register, name='member_register'),
    path('profile/', views.profile, name='member_profile'),
    path('logout/', views.auth_logout, name='member_logout'),
    path('members/', views.memberlist, name='member_list'),
    path('searched/', views.searchmember, name='search_member'),
    path('Edit/', views.edit_profile, name='edit_profile'),
    path('Edited', views.editing_profile, name='edited_profile'),
    path('delete_profile', views.delete, name='delete_profile')
]