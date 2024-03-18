from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Freelancer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

