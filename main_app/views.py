from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


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

# Auth
def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

