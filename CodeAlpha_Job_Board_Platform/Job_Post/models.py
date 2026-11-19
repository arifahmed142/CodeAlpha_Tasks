from django.db import models

# Create your models here.
class JobPost(models.Model):
    employer = models.ForeignKey('Users.employer',on_delete=models.CASCADE,related_name='job_posts')

    job_title = models.CharField(max_length=100)
    job_category = models.CharField(max_length=100)
    job_type = models.CharField(max_length=20,default='FULL-TIME')
    job_location = models.CharField(max_length=150)
    workplace_type = models.CharField(max_length=20,default='ON-SITE')

    job_description = models.TextField()
    responsibilities = models.TextField()
    requirements = models.TextField()
    qualifications = models.TextField(blank=True, null=True)
    benefits = models.TextField(blank=True, null=True)
    required_skills = models.TextField(blank=True, null=True)


    salary_min = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    salary_max = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    salary_currency = models.CharField(max_length=10, default='BDT')
    vacancies = models.PositiveIntegerField(default=1)
    experience_required = models.CharField(max_length=50, blank=True, null=True)

    application_deadline = models.DateField()
    application_email = models.EmailField(blank=True, null=True)

    job_status = models.CharField(max_length=15,default='OPEN TO APPLY')


    posted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
