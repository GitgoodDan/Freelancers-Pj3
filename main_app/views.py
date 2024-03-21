from typing import Any
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

# def job_subcategory(request, subcategory_id):
#   subcategory = JobPosting.objects.get(category=subcategory_id)
#   return render(request, 'jobposting/subcategory.html', {'subcategory': subcategory})
def subCategories(request):
  return render(request, 'categories/subCategories.html')

def graphic_design_index(request):
   return render(request, 'categories/graphic_design.html')

def logo_design_jobs(request):
   jobpostings_GD1 = JobPosting.objects.filter(category = 'logo_design').values()
   return render(request, 'graphic_design/logo_design_jobs.html', {'jobpostings_GD1': jobpostings_GD1})

def web_ui_design_jobs(request):
   jobpostings_GD2 = JobPosting.objects.filter(category = 'web_ui_design').values()
   return render(request, 'graphic_design/web_ui_design_jobs.html', {'jobpostings_GD2': jobpostings_GD2})

def mobile_ui_design_jobs(request):
   jobpostings_GD3 = JobPosting.objects.filter(category = 'mobile_ui_design').values()
   return render(request, 'graphic_design/mobile_ui_design_jobs.html', {'jobpostings_GD3': jobpostings_GD3})

def illustration_jobs(request):
   jobpostings_GD4 = JobPosting.objects.filter(category = 'illustration').values()
   return render(request, 'graphic_design/illustration_jobs.html', {'jobpostings_GD4': jobpostings_GD4})

def email_design_jobs(request):
   jobpostings_GD5 = JobPosting.objects.filter(category = 'email_design').values()
   return render(request, 'graphic_design/email_design_jobs.html', {'jobpostings_GD5': jobpostings_GD5})

def infographics_design_jobs(request):
   jobpostings_GD6 = JobPosting.objects.filter(category = 'infographics_design').values()
   return render(request, 'graphic_design/infographics_design_jobs.html', {'jobpostings_GD6': jobpostings_GD6})

def branding_and_identity_design_jobs(request):
   jobpostings_GD7 = JobPosting.objects.filter(category = 'branding_and_identity_design').values()
   return render(request, 'graphic_design/branding_and_identity_design_jobs.html', {'jobpostings_GD7': jobpostings_GD7})

def web_dev_index(request):
    return render(request, 'categories/web_dev.html')

def front_end_development_jobs(request):
   jobpostings_WD1 = JobPosting.objects.filter(category = 'front_end_development').values()
   return render(request, 'web_dev/front_end_development_jobs.html', {'jobpostings_WD1': jobpostings_WD1})

def back_end_development_jobs(request):
   jobpostings_WD2 = JobPosting.objects.filter(category = 'back_end_development').values()
   return render(request, 'web_dev/back_end_development_jobs.html', {'jobpostings_WD2': jobpostings_WD2})

def full_stack_development_jobs(request):
   jobpostings_WD3 = JobPosting.objects.filter(category = 'full_stack_development').values()
   return render(request, 'web_dev/full_stack_development_jobs.html', {'jobpostings_WD3': jobpostings_WD3})

def e_commerce_development_jobs(request):
   jobpostings_WD4 = JobPosting.objects.filter(category = 'e_commerce_development').values()
   return render(request, 'web_dev/e_commerce_development_jobs.html', {'jobpostings_WD4': jobpostings_WD4})

def web_application_development_jobs(request):
   jobpostings_WD5 = JobPosting.objects.filter(category = 'web_application_development').values()
   return render(request, 'web_dev/web_application_development_jobs.html', {'jobpostings_WD5': jobpostings_WD5})

def responsive_web_design_jobs(request):
   jobpostings_WD6 = JobPosting.objects.filter(category = 'responsive_web_design').values()
   return render(request, 'web_dev/responsive_web_design_jobs.html', {'jobpostings_WD6': jobpostings_WD6})

def digital_marketing_index(request):
   return render(request, 'categories/digital_marketing.html')

def search_engine_optimization_jobs(request):
   jobpostings_DM1 = JobPosting.objects.filter(category = 'search_engine_optimization').values()
   return render(request, 'digital_marketing/search_engine_optimization_jobs.html', {'jobpostings_DM1': jobpostings_DM1})

def social_media_marketing_jobs(request):
   jobpostings_DM2 = JobPosting.objects.filter(category = 'social_media_marketing').values()
   return render(request, 'digital_marketing/social_media_marketing_jobs.html', {'jobpostings_DM2': jobpostings_DM2})

def pay_per_click_advertising_jobs(request):
   jobpostings_DM3 = JobPosting.objects.filter(category = 'pay_per_click_advertising').values()
   return render(request, 'digital_marketing/pay_per_click_advertising_jobs.html', {'jobpostings_DM3': jobpostings_DM3})

def content_marketing_jobs(request):
   jobpostings_DM4 = JobPosting.objects.filter(category = 'content_marketing').values()
   return render(request, 'digital_marketing/content_marketing_jobs.html', {'jobpostings_DM4': jobpostings_DM4})

def email_marketing_jobs(request):
   jobpostings_DM5 = JobPosting.objects.filter(category = 'email_marketing').values()
   return render(request, 'digital_marketing/email_marketing_jobs.html', {'jobpostings_DM5': jobpostings_DM5})

def influencer_marketing_jobs(request):
   jobpostings_DM6 = JobPosting.objects.filter(category = 'influencer_marketing').values()
   return render(request, 'digital_marketing/influencer_marketing_jobs.html', {'jobpostings_DM6': jobpostings_DM6})

def online_reputation_management_jobs(request):
   jobpostings_DM7 = JobPosting.objects.filter(category = 'online_reputation_management').values()
   return render(request, 'digital_marketing/online_reputation_management_jobs.html', {'jobpostings_DM7': jobpostings_DM7})

def mobile_app_dev_index(request):
    return render(request, 'categories/mobile_app_dev.html')

def ios_app_development_jobs(request):
    jobpostings_MAD1 = JobPosting.objects.filter(category = 'ios_app_development').values()
    return render(request, 'mobile_app_dev/ios_app_development_jobs.html', {'jobpostings_MAD1': jobpostings_MAD1})

def andriod_app_development_jobs(request):
    jobpostings_MAD2 = JobPosting.objects.filter(category = 'andriod_app_development').values()
    return render(request, 'mobile_app_dev/andriod_app_development_jobs.html', {'jobpostings_MAD2': jobpostings_MAD2})

def cross_platform_app_development_jobs(request):
    jobpostings_MAD3 = JobPosting.objects.filter(category = 'cross_platform_app_development').values()
    return render(request, 'mobile_app_dev/cross_platform_app_development_jobs.html', {'jobpostings_MAD3': jobpostings_MAD3})

def mobile_game_development_jobs(request):
    jobpostings_MAD4 = JobPosting.objects.filter(category = 'mobile_game_development').values()
    return render(request, 'mobile_app_dev/mobile_game_development_jobs.html', {'jobpostings_MAD4': jobpostings_MAD4})

def app_testing_and_quality_assurance_jobs(request):
    jobpostings_MAD5 = JobPosting.objects.filter(category = 'app_testing_and_quality_assurance').values()
    return render(request, 'mobile_app_dev/app_testing_and_quality_assurance_jobs.html', {'jobpostings_MAD5': jobpostings_MAD5})

def app_maintenance_and_updates_jobs(request):
    jobpostings_MAD6 = JobPosting.objects.filter(category = 'app_maintenance_and_updates').values()
    return render(request, 'mobile_app_dev/app_maintenance_and_updates_jobs.html', {'jobpostings_MAD6': jobpostings_MAD6})

def cybersecurity_index(request):
   return render(request, 'categories/cybersecurity.html')

def network_security_jobs(request):
   jobpostings_CS1 = JobPosting.objects.filter(category = 'network_security').values()
   return render(request, 'cybersecurity/network_security_jobs.html', {'jobpostings_CS1': jobpostings_CS1})

def ethical_hacking_jobs(request):
   jobpostings_CS2 = JobPosting.objects.filter(category = 'ethical_hacking').values()
   return render(request, 'cybersecurity/ethical_hacking_jobs.html', {'jobpostings_CS2': jobpostings_CS2})

def penetration_testing_jobs(request):
   jobpostings_CS3 = JobPosting.objects.filter(category = 'penetration_testing').values()
   return render(request, 'cybersecurity/penetration_testing_jobs.html', {'jobpostings_CS3': jobpostings_CS3})

def security_auditing_jobs(request):
   jobpostings_CS4 = JobPosting.objects.filter(category = 'security_auditing').values()
   return render(request, 'cybersecurity/security_auditing_jobs.html', {'jobpostings_CS4': jobpostings_CS4})

def data_encryption_jobs(request):
   jobpostings_CS5 = JobPosting.objects.filter(category = 'data_encryption').values()
   return render(request, 'cybersecurity/data_encryption_jobs.html', {'jobpostings_CS5': jobpostings_CS5})

def incident_response_jobs(request):
   jobpostings_CS6 = JobPosting.objects.filter(category = 'incident_response').values()
   return render(request, 'cybersecurity/incident_response_jobs.html', {'jobpostings_CS6': jobpostings_CS6})

def security_compliance_jobs(request):
   jobpostings_CS7 = JobPosting.objects.filter(category = 'security_compliance').values()
   return render(request, 'cybersecurity/security_compliance_jobs.html', {'jobpostings_CS7': jobpostings_CS7})

def register(request):
  return render(request, 'registration/register.html')

def reg_client(request):
  return render(request, 'register/client.html')

def reg_freelancer(request):
  return render(request, 'register/freelancer.html')

def profile_client(request, client_id):
  client = ClientProfile.objects.get(id=client_id)
  return render(request, 'profile/client.html', {'client': client})

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
  fields = ['title', 'description', 'price', 'category', 'location', 'timeframe']
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
        messages.info(request, f"Price range: ${', '.join(price_filter)}")

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

def freelancer_public(request, freelancer_id):
    freelancer = FreelancerProfile.objects.get(id=freelancer_id)
    return render(request, 'freelancer/public.html', {'freelancer': freelancer})