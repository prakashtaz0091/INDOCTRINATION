from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50, default="")
    address = models.CharField( max_length=70,null=False)
    phoneNo = models.CharField(max_length=30,null=False)
    level = models.CharField(max_length=20,null=False)
    registeredAt = models.DateTimeField(auto_now_add=True)
    dob = models.DateField()
    disability = models.CharField( max_length=10,null=True,blank=True)
    bio = models.TextField(default="",null=True,blank=True)
    
