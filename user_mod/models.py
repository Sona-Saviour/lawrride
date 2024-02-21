from django.db import models
from advocate_mod.models import *

# Create your models here.
class user(models.Model):
    uname=models.CharField(max_length=15)
    uemail=models.EmailField()
    phone=models.IntegerField()
    password=models.CharField(max_length=10, null=True)

class appointment(models.Model):
    uid=models.ForeignKey(user, on_delete=models.CASCADE, null=True)
    aid=models.ForeignKey(advocate, on_delete=models.CASCADE, null=True)
    date_time=models.DateTimeField()
    ap_name=models.CharField(max_length=15, null=True)
    ap_email=models.EmailField(null=True)
    ap_aname=models.CharField(max_length=50, null=True)
    appointment=models.CharField(max_length=50,default="waiting for approval")

class complaint(models.Model):
    cname=models.CharField(max_length=20)
    cemail=models.EmailField()
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=400)
   
