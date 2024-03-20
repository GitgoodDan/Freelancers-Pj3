from django.contrib import admin
from .models import JobPosting, ClientProfile, FreelancerProfile

# Register your models here.
admin.site.register(ClientProfile)
admin.site.register(FreelancerProfile)
admin.site.register(JobPosting)