from django.contrib import admin
from .models import employer, profile, candidate

# Register your models here.
admin.site.register(profile)
admin.site.register(candidate)
admin.site.register(employer)