from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=100)
    emailid = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    confirmpassword = models.CharField(max_length=100)
    
  

    def __str__(self):
        return self.name
    

    