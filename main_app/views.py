from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

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

def profile_client(request):
  # client = Client.objects.get(id=client_id)
  return render(request, 'profile/client.html', {})

def profile_freelancer(request):
  # freelancer = Freelancer.objects.get(id=freelancer_id)
  return render(request, 'profile/freelancer.html', {})

# class JobCreate(CreateView):
#   model = JobPosting
#   fields = '__all__'

# class JobUpdate(UpdateView):
#   model = JobPosting
#   fields = []

# class JobDelete(DeleteView):
#   model = JobPosting

# class JobList(ListView):
#   model = JobPosting

# class JobDetail(DetailView):
#   model = JobPosting
