from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from django.contrib.auth import login
# from django.contrib.auth.forms import UserCreationForm

from .forms import ClientSignUpForm, FreelancerSignUpForm

from .models import JobPosting, ClientProfile, FreelancerProfile

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def categories(request):
  return render(request, 'categories/index.html')

def listings(request):
  return render(request, 'categories/listings.html')

def register(request):
  return render(request, 'registration/register.html')

def reg_client(request):
  return render(request, 'register/client.html')

def reg_freelancer(request):
  return render(request, 'register/freelancer.html')

def profile_client(request, client_id):
  client = ClientProfile.objects.get(id=client_id)
  return render(request, 'profile/client.html', {'client': client})


def profile_freelancer(request, freelancer_id):
  freelancer = FreelancerProfile.objects.get(id=freelancer_id)
  return render(request, 'profile/freelancer.html', {'freelancer': freelancer})

class ClientUpdate(UpdateView):
   model = ClientProfile
   fields = ['address', 'company', 'phone_number']

class ClientDelete(DeleteView):
   model = ClientProfile
   success_url = '/register'

def profile_freelancer(request, freelancer_id):
  freelancer = FreelancerProfile.objects.get(id=freelancer_id)
  return render(request, 'profile/freelancer.html', {'freelancer' : freelancer})

class FreelancerUpdate(UpdateView):
   model = FreelancerProfile
   fields = ['skills', 'portfolio_link', 'hourly_rate', 'type_fl']

class FreelancerDelete(DeleteView):
   model = FreelancerProfile
   success_url = '/register'


def job_detail(request, jobposting_id):
  jobposting = JobPosting.objects.get(id=jobposting_id)
  return render(request, 'jobposting/detail.html', {'jobposting': jobposting})

class JobCreate(CreateView):
  model = JobPosting
  fields = ['title', 'description', 'price']
  success_url = '/posting/list'

class JobUpdate(UpdateView):
  model = JobPosting
  fields = ['title', 'description', 'price']

class JobDelete(DeleteView):
  model = JobPosting
  success_url = '/'

class JobList(ListView):
  model = JobPosting

def signup(request):
    return render(request, 'registration/register.html')

def client_signup(request):
    if request.method == 'POST':
        form = ClientSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = ClientSignUpForm()
    
    return render(request, 'registration/client_signup.html', {'form': form})

def freelancer_signup(request):
    if request.method == 'POST':
        form = FreelancerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = FreelancerSignUpForm()
    
    return render(request, 'registration/freelancer_signup.html', {'form': form})