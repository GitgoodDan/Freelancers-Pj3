from django.db import models
from django.contrib.auth.models import User, AbstractUser, Group, Permission

# Create your models here.

class UserProfile(AbstractUser):
    CLIENT_ROLE = 'client'
    FREELANCER_ROLE = 'freelancer'
    USER_ROLES = [
        (CLIENT_ROLE, 'Client'),
        (FREELANCER_ROLE, 'Freelancer'),
    ]

    role = models.CharField(max_length=15, choices=USER_ROLES)
    location = models.CharField(max_length=100)
    
    groups = models.ManyToManyField(Group, related_name='user_profiles')
    user_permissions = models.ManyToManyField(Permission, related_name='user_profiles')

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    public_contact_info = models.CharField(max_length=255)

    def __str__(self):
        return self.company_name

class Freelancer(models.Model):
    FREELANCER_TYPES = [
        ('graphic_designer', 'Graphic Designer'),
        ('front_end_developer', 'Front-End Developer'),
        ('back_end_developer', 'Back-End Developer'),
        ('full_stack_developer', 'Full Stack Developer'),
    ]


    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    skills = models.CharField(max_length=255)
    base_rate = models.DecimalField(max_digits=8, decimal_places=2)
    type_fl = models.CharField(max_length=20, choices=FREELANCER_TYPES)

    def __str__(self):
        return self.user.username

class JobPosting(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='job_postings')
    freelancer = models.ForeignKey(Freelancer, on_delete=models.SET_NULL, blank=True, null=True, related_name='job_applications')
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    
