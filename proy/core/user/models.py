from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    rut = models.CharField(max_length=15)

  


    
  
