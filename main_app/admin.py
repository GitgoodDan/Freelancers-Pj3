from django.contrib import admin
from .models import JobPosting, UserProfile, ClientProfile, FreelancerProfile

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(ClientProfile)
admin.site.register(FreelancerProfile)
admin.site.register(JobPosting)