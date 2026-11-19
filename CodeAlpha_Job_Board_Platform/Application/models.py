from django.db import models


class Application(models.Model):

    job = models.ForeignKey('Job_Post.JobPost',on_delete=models.CASCADE,related_name='applications')
    candidate = models.ForeignKey('Users.candidate',on_delete=models.CASCADE,related_name='applications')

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255, blank=True, null=True)
    resume = models.FileField(upload_to='applications/resumes/')
    cover_letter = models.TextField()
    experience = models.PositiveIntegerField(default=0)
    expected_salary = models.DecimalField(max_digits=12,decimal_places=2,blank=True,null=True)
    application_status = models.CharField(max_length=20,default='PENDING')

    applied_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('job', 'candidate')
        ordering = ['-applied_at']
