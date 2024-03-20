from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('categories/', views.categories, name='categories'),
    path('categories/', views.categories, name='categories'),
    path('categories/subCategories/', views.subCategories, name='subCategories'),
    path('register/', views.register, name='register'),
    path('register/client/', views.reg_client, name='reg_client'),
    path('register/freelancer/', views.reg_freelancer, name='reg_freelancer'),
    path('client_signup/', views.client_signup, name='client_signup'),
    path('freelancer_signup/', views.freelancer_signup, name='freelancer_signup'),
    path('posting/create/', views.JobCreate.as_view(), name='posting_create'),
    path('posting/update/', views.JobUpdate.as_view(), name='posting_update'),
    path('posting/delete/', views.JobDelete.as_view(), name='posting_delete'),
    path('posting/list/', views.JobList.as_view(), name='posting_list'),
    path('posting/<int:jobposting_id>/', views.job_detail, name='posting_detail'),
    path('profile/client/<int:client_id>', views.profile_client, name='prof_client'),
    path('profile/client/<int:pk>/update', views.ClientUpdate.as_view(), name='client_update'),
    path('profile/client/<int:pk>/delete', views.ClientDelete.as_view(), name='client_delete'),    
    path('profile/freelancer/<int:freelancer_id>/', views.profile_freelancer, name='prof_freelancer'),
    path('profile/freelancer/<int:pk>/update', views.FreelancerUpdate.as_view(), name='freelancer_update'),
    path('profile/freelancer/<int:pk>/delete', views.FreelancerDelete.as_view(), name='freelancer_delete'),
    path('profile/freelancer/', views.all_freelancers, name='all_freelancers'),

]