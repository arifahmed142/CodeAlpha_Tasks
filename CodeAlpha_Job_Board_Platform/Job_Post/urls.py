from django.urls import path
from . import views

urlpatterns = [
    path('', views.JobPosts, name='Home'),
    path('Job_Details/<int:id>/', views.JobDetails, name='Details'),
    path('Job-List', views.MyPostedJobs, name='Job_List'),
    path('post-job/', views.PostJob, name='PostJob'),
    path('Applicants/<int:id>/', views.Applicants, name='Applicant'),
    path('onsite/', views.onsite, name='onsite'),
    path('internship/', views.intern, name='Intern'),
    path('remote/', views.remote, name='remote'),
]