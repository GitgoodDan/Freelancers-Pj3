from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
# from django.contrib.auth.forms import UserCreationForm
from .forms import ClientSignUpForm, FreelancerSignUpForm
from .models import JobPosting, ClientProfile, FreelancerProfile, User
from django.db.models import Q
from django.contrib import messages

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def categories(request):
  return render(request, 'categories/index.html')

def subCategories(request):
  return render(request, 'categories/subCategories.html')

def graphic_design_index(request):
   jobpostings_GD = JobPosting.objects.filter(category = 'graphic_design').values()
   print(jobpostings_GD)
   return render(request, 'categories/graphic_design.html', {'jobpostings_GD': jobpostings_GD})

def web_dev_index(request):
   jobpostings_WD = JobPosting.objects.filter(category = 'web_development').values()
   return render(request, 'categories/web_dev.html', {'jobpostings_WD': jobpostings_WD})

def digital_marketing_index(request):
   jobpostings_DM = JobPosting.objects.filter(category = 'digital_marketing').values()
   return render(request, 'categories/digital_marketing.html', {'jobpostings_DM': jobpostings_DM})

def mobile_app_dev_index(request):
   jobpostings_MAD = JobPosting.objects.filter(category = 'mobile_app_development').values()
   return render(request, 'categories/mobile_app_dev.html', {'jobpostings_MAD': jobpostings_MAD})

def cybersecurity_index(request):
   jobpostings_CS = JobPosting.objects.filter(category = 'cyber_security').values()
   return render(request, 'categories/cybersecurity.html', {'jobpostings_CS': jobpostings_CS})

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


# def profile_freelancer(request, freelancer_id):
#   freelancer = FreelancerProfile.objects.get(id=freelancer_id)
#   return render(request, 'profile/freelancer.html', {'freelancer': freelancer})

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


def job_detail(request, job_id):
  job = JobPosting.objects.get(id=job_id)
  return render(request, 'jobposting/detail.html', {'job': job})

class JobCreate(LoginRequiredMixin, CreateView):
  model = JobPosting
  fields = ['title', 'description', 'price', 'category', 'location']
  def form_valid(self, form):
     job = form.save(commit=False)
     job.client=self.request.user
     job.save()
     return redirect('/')

class JobUpdate(LoginRequiredMixin, UpdateView):
  model = JobPosting
  fields = ['title', 'description', 'price', 'category', 'location']

class JobDelete(LoginRequiredMixin, DeleteView):
  model = JobPosting
  success_url = '/'

class JobList(ListView):
  model = JobPosting
  template_name = 'jobposting_list.html'
  context_object_name = 'jobpostings'


def job_search(request):
  query = request.GET.get('q')
  if query:
    jobs = JobPosting.objects.filter(title__icontains=query)
  else: jobs = JobPosting.objects.all()
  return render(request, 'job_search.html', {'jobs': jobs})

def job_search_wd(request):
    query = request.GET.get('q')
    if query:
        jobs = JobPosting.objects.filter(category='web_development', title__icontains=query)
    else:
        jobs = JobPosting.objects.filter(category='web_development')
    return render(request, 'job_search_wd.html', {'jobs': jobs, 'category': 'Web Development'})

def job_search_gd(request):
    query = request.GET.get('q')
    if query:
        jobs = JobPosting.objects.filter(category='graphic_design', title__icontains=query)
    else:
        jobs = JobPosting.objects.filter(category='graphic_design')
    return render(request, 'job_search_wd.html', {'jobs': jobs, 'category': 'Graphic Design'})

def job_search_dm(request):
    query = request.GET.get('q')
    if query:
        jobs = JobPosting.objects.filter(category='digital_marketing', title__icontains=query)
    else:
        jobs = JobPosting.objects.filter(category='digital_marketing')
    return render(request, 'job_search_wd.html', {'jobs': jobs, 'category': 'Digital Marketing'})

def job_search_mad(request):
    query = request.GET.get('q')
    if query:
        jobs = JobPosting.objects.filter(category='mobile_app_development', title__icontains=query)
    else:
        jobs = JobPosting.objects.filter(category='mobile_app_development')
    return render(request, 'job_search_wd.html', {'jobs': jobs, 'category': 'Mobile App Development'})

def job_search_cs(request):
    query = request.GET.get('q')
    if query:
        jobs = JobPosting.objects.filter(category='cyber_security', title__icontains=query)
    else:
        jobs = JobPosting.objects.filter(category='cyber_security')
    return render(request, 'job_search_wd.html', {'jobs': jobs, 'category': 'Cyber Security'})

def signup(request):
    return render(request, 'registration/register.html')

def client_signup(request):
    if request.method == 'POST':
        form = ClientSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create ClientProfile and associate it with the user
            client_profile = ClientProfile(user=user)
            client_profile.save()
            login(request, user)
            return redirect('home')
    else:
        form = ClientSignUpForm()
    
    return render(request, 'registration/client_signup.html', {'form': form})
    

def freelancer_signup(request):
    if request.method == 'POST':
        form = FreelancerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']  # Get the password separately
            user.set_password(password)  # Set the password
            user.save()

            freelancer_profile = FreelancerProfile(
                user=user,
                skills=form.cleaned_data['skills'],
                portfolio_link=form.cleaned_data['portfolio_link'],
                hourly_rate=form.cleaned_data['hourly_rate'],
                delivery_time=form.cleaned_data['delivery_time'],
                located=form.cleaned_data['located'],
                type_fl=form.cleaned_data['type_fl']
            )
            freelancer_profile.save()

            login(request, user)
            return redirect('home')
    else:
        form = FreelancerSignUpForm()
    
    return render(request, 'registration/freelancer_signup.html', {'form': form})

def all_freelancers(request):
    # Retrieve all FreelancerProfile objects from the database
    freelancers = FreelancerProfile.objects.all()
    # Filter based on price range
    price_filter = request.GET.getlist('price')
    price_query = Q()
    for price in price_filter:
        if price == 'under20':
            price_query |= Q(hourly_rate__lt=20)
        elif price == '20to50':
            price_query |= Q(hourly_rate__range=[20, 50])
        elif price == '50to100':
            price_query |= Q(hourly_rate__range=[50, 100])
        elif price == 'over100':
            price_query |= Q(hourly_rate__gt=100)

    if price_query:
        freelancers = freelancers.filter(price_query)
        messages.info(request, f"Price range: {', '.join(price_filter)}")

    # Filter based on delivery time
    delivery_filter = request.GET.get('delivery')
    if delivery_filter:
        freelancers = freelancers.filter(delivery_time=delivery_filter)
        messages.info(request, f"Delivery time: {delivery_filter}")

    # Filter based on location
    location_filter = request.GET.get('country')
    if location_filter:
        freelancers = freelancers.filter(located=location_filter)
        messages.info(request, f"Location: {location_filter}")

    context = {
        'freelancers': freelancers
    }
    return render(request, 'freelancer/all_freelancers.html', context)