from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager,PermissionsMixin)

# Create your models here.
class User_template(BaseUserManager):
    def create_user(self, email,name,phone,password, **extra_fields):
        if not email:
            raise ValueError("Email is Required!")
        email = email.strip().lower()
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        user = self.model(
            email = email,
            name = name,
            phone = phone,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,name,phone,password,**extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        return self.create_user(
            email=email,
            name=name,
            phone=phone,
            password=password,
            **extra_fields
        )

class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=11)
    is_staff = models.BooleanField(default=False)
    profile_photo = models.ImageField(
        upload_to="Profiles/",
        blank=True,
        null=True
    )

    is_active = models.BooleanField(default=True)

    objects = User_template()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name","phone"]

    def __str__(self):
        return self.email