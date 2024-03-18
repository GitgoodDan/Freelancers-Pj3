from django.contrib import admin
from .models import JobPosting, UserProfile, Client, Freelancer

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Client)
admin.site.register(Freelancer)
admin.site.register(JobPosting)