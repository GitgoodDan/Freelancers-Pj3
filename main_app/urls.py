from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('categories/', views.categories, name='categories'),
    # path('categories/<>', views.listings, name='listings'),

    # path('register/', views.register, name='register'),
    # path('register/client/', views.reg_client, name='reg_client'),
    # path('register/freelancer/', views.reg_freelancer, name='reg_freelancer'),

    # path('profile/client/<int:client_id>', views.profile_client, name='prof_client'),
    # path('profile/freelancer/<int:freelancer_id>', views.profile_freelancer, name='prof_freelancer'),
=========
>>>>>>>>> Temporary merge branch 2
]