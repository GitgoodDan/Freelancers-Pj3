from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    company = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    def get_absolute_url(self):
        return reverse('prof_client', kwargs={'client_id': self.id})
    # Add more fields as needed for client profiles

    def __str__(self):
        return self.user.username
    

class FreelancerProfile(models.Model):
    FREELANCER_TYPES = [
        ('graphic_designer', 'Graphic Designer'),
        ('front_end_developer', 'Front-End Developer'),
        ('back_end_developer', 'Back-End Developer'),
        ('full_stack_developer', 'Full Stack Developer'),
    ]
    LOCATION_TYPES = [  
        ('us_only', 'US Only'),
        ('worldwide', 'Worldwide'),
    ]
    DELIVERY_TYPES = [  
        ('express', 'Express 24hrs'),
        ('up_3_days', 'Up to 3 days'),
        ('up_7_days', 'Up to 7 days'),
        ('anytime', 'Anytime'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.TextField()
    portfolio_link = models.URLField()
    hourly_rate = models.DecimalField(max_digits=8, decimal_places=2)
    delivery_time = models.CharField(max_length=20, choices=DELIVERY_TYPES)
    located = models.CharField(max_length=20, choices=LOCATION_TYPES)
    type_fl = models.CharField(max_length=20, choices=FREELANCER_TYPES)
    
    def get_absolute_url(self):
        return reverse('prof_freelancer', kwargs={'freelancer_id': self.id})
    # Add more fields as needed for freelancer profiles
    type_fl = models.CharField(max_length=20, choices=FREELANCER_TYPES)

    def __str__(self):
        return self.user.username


class JobPosting(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_postings')
    freelancer = models.ForeignKey(FreelancerProfile, on_delete=models.SET_NULL, blank=True, null=True, related_name='job_applications')
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    JOB_CATEGORIES = [
        ('graphic_design', 'Graphic Design'),
        ('web_development', 'Web Development'),
        ('digital_marketing', 'Digital Marketing'),
        ('mobile_app_development', 'Mobile App Development'),
        ('cyber_security', 'Cyber Security')
    ]
    category = models.CharField(
        choices=JOB_CATEGORIES, 
        max_length=24,
        default=JOB_CATEGORIES[0][0])
    JOB_LOCATIONS = [
        ('united_states', 'United States'),
        ('worldwide', 'Worldwide')
    ]
    location = models.CharField(
        choices=JOB_LOCATIONS, 
        max_length=16,
        default=JOB_LOCATIONS[0][0])
