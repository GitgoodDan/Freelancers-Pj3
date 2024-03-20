from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User, AbstractUser, Group, Permission


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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.TextField()
    portfolio_link = models.URLField()
    hourly_rate = models.DecimalField(max_digits=8, decimal_places=2)
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
        # Graphic Design
        ('logo_design', 'Logo Design'),
        ('web_ui_design', 'Web U/I Design'),
        ('mobile_ui_design', 'Mobile U/I Design'),
        ('illustration', 'Illustration'),
        ('email_design', 'Email Design'),
        ('infographics_design', 'Infographics Design'),
        ('branding_and_identity_design', 'Branding and Identity Design'),
        # Web Development
        ('front_end_development', 'Front-End Development'),
        ('back_end_development', 'Back-End Development'),
        ('full_stack_development', 'Full-Stack Development'),
        ('e_commerce_development', 'E-Commerce Development'),
        ('web_application_development', 'Web Application Development'),
        ('responsive_web_design', 'Responsive Web Design'),
        # Digital Marketing
        ('search_engine_optimization', 'Search Engine Optimization (SEO)'),
        ('social_media_marketing', 'Social Media Marketing'),
        ('pay_per_click_advertising', 'Pay-Per-Click (PPC) Advertising'),
        ('content_marketing', 'Content Marketing'),
        ('email_marketing', 'Email Marketing'),
        ('influencer_marketing', 'Influencer Marketing'),
        ('online_reputation_management', 'Online Reputation Management'),
        # Mobile App Development
        ('ios_app_development', 'iOS App Development'),
        ('andriod_app_development', 'Android App Development'),
        ('cross_platform_app_development', 'Android App Development'),
        ('mobile_game_development', 'Mobile Game Development'),
        ('app_testing_and_quality_assurance', 'App Testing and Quality Assurance'),
        ('app_maintenance_and_updates', 'App Maintenance and Updates'),
        # Cyber Security
        ('network_security', 'Network Security'),
        ('ethical_hacking', 'Ethical Hacking'),
        ('penetration_testing', 'Penetration Testing'),
        ('security_auditing', 'Security Auditing'),
        ('data_encription', 'Data Encryption'),
        ('incident_response', 'Incident Response'),
        ('security_compliance', 'Security Compliance')
    ]
    category = models.CharField(
        choices=JOB_CATEGORIES, 
        max_length=33,
        default=JOB_CATEGORIES[0][0])
    JOB_LOCATIONS = [
        ('united_states', 'United States'),
        ('worldwide', 'Worldwide')
    ]
    location = models.CharField(
        choices=JOB_LOCATIONS, 
        max_length=16,
        default=JOB_LOCATIONS[0][0])
    TIMEFRAME_OPTIONS = [
        ('1to3months', '1 - 3 Months'),
        ('3to6months', '3 - 6 Months'),
        ('morethan6months', 'More than 6 months')
    ]
    timeframe = models.CharField(
        choices=TIMEFRAME_OPTIONS, 
        max_length=24,
        default=JOB_CATEGORIES[0][0])

