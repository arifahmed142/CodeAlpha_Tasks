from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

# Create your models here.
class manager(BaseUserManager):
    def create_user(self,email,username,password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required!')
        email = self.normalize_email(email)
        user = self.model(
            email = email,
            username = username,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)
        return self.create_user(email,username,password,**extra_fields)

class profile(AbstractBaseUser,PermissionsMixin):
    name = models.CharField(max_length=30, blank=False, null=False)
    username = models.CharField(max_length=30, primary_key=True)
    phone = models.CharField(max_length=11, blank=False, unique=True)
    present_address = models.CharField(max_length=200,blank=True, null=True)
    permanent_address = models.CharField(max_length=200,blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profile/photo', blank=True, null=True)
    email = models.EmailField(max_length=50, unique=True, blank=False, null=False)
    nationality = models.CharField(max_length=20,null=True,blank=True)
    blood_group = models.CharField(max_length=2,null=True,blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = manager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','phone']

class candidate(profile):
    is_candidate = models.BooleanField(default=True)
    is_employer = models.BooleanField(default=False)
    ssc_board = models.CharField(max_length=20, null=True, blank=True)
    ssc_institution = models.CharField(max_length=100, null=True, blank=True)
    ssc_result = models.CharField(max_length=4,null=True,blank=True)
    hsc_board = models.CharField(max_length=20, null=True, blank=True)
    hsc_institution = models.CharField(max_length=100, null=True, blank=True)
    hsc_result = models.CharField(max_length=4,null=True,blank=True)
    resume = models.FileField(upload_to='profile/resume', blank=True, null=True)

class employer(profile):
    is_candidate = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=True)
    working_company = models.CharField(max_length=100, blank=True, null=True)
    designation = models.CharField(max_length=50, blank=True, null=True)
    working_time = models.CharField(max_length=10, blank=True, null=True)
    cv = models.FileField(upload_to='profile/cv', blank=True, null=True)
    