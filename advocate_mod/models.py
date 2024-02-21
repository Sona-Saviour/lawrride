from django.db import models

# Create your models here.
class advocate(models.Model):
    aname=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    email=models.EmailField()
    phone_no=models.IntegerField()
    about=models.CharField(max_length=1000)
    image=models.ImageField(upload_to="advocates") 
    status=models.CharField(max_length=30,default="waiting for approval")
    password=models.CharField(max_length=8, null=True)