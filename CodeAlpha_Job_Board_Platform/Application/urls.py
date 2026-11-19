from django.urls import path
from . import views

urlpatterns = [
    path('Application/<int:id>/', views.application, name='Application'),
    path('Applied-List/', views.applied ,name='Applied'),
    path('Application-Details/<int:id>/', views.ApplicationDetails, name='Application_Details')
]