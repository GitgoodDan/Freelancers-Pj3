from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models import ClientProfile, FreelancerProfile

class ClientSignUpForm(UserCreationForm):
    address = forms.CharField(max_length=255)
    company = forms.CharField(max_length=20)
    phone_number = forms.CharField(max_length=20)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name', 'address', 'company', 'phone_number')


class FreelancerSignUpForm(UserCreationForm):
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

    skills = forms.CharField(max_length=255)
    portfolio_link = forms.URLField()
    hourly_rate = forms.DecimalField(max_digits=8, decimal_places=2)
    delivery_time = forms.ChoiceField(choices=DELIVERY_TYPES, widget=forms.Select())
    type_fl = forms.ChoiceField(choices=FREELANCER_TYPES, widget=forms.Select())
    located = forms.ChoiceField(choices=LOCATION_TYPES, widget=forms.Select())
    
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name', 'skills', 'portfolio_link', 'hourly_rate', 'delivery_time', 'located', 'type_fl')