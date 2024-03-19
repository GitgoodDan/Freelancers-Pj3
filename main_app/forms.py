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
    skills = forms.CharField(max_length=255)
    portfolio_link = forms.URLField()
    hourly_rate = forms.DecimalField(max_digits=8, decimal_places=2)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name', 'skills', 'portfolio_link', 'hourly_rate')