from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Client, Freelancer, JobPosting

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
  return render(request, 'register/index.html')

def reg_client(request):
  return render(request, 'register/client.html')

def reg_freelancer(request):
  return render(request, 'register/freelancer.html')

def profile_client(request, client_id):
  client = Client.objects.get(id=client_id)
  return render(request, 'profile/client.html', {'client': client})

def profile_freelancer(request, freelancer_id):
  freelancer = Freelancer.objects.get(id=freelancer_id)
  return render(request, 'profile/freelancer.html', {'freelancer': freelancer})

def job_detail(request, job_id):
  job = JobPosting.objects.get(id=job_id)
  return render(request, 'jobposting/detail.html', {'job': job})

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

class JobDetail(DetailView):
  model = JobPosting