from django.db import models
from django.db import IntegrityError
from django.contrib.auth.models import User

class users(models.Model):
    Email_id=models.CharField(max_length=30)
    password=models.CharField(max_length=20)
    username=models.CharField(max_length=30)
    ph_no=models.IntegerField()
    gender=models.CharField(max_length=30)
class frequests(models.Model):
    rid=models.AutoField(primary_key=True)
    sender=models.CharField(max_length=40)
    reciever=models.CharField(max_length=40)
    status=models.IntegerField()

class wallpost(models.Model):
    id=models.AutoField(primary_key=True)
    sender=models.CharField(max_length=50)
    message=models.CharField(max_length=110)
class Player_Profile(models.Model):
    name=models.CharField(max_length=50,null=True)
    email=models.EmailField(max_length=50)
    profile_picture=models.ImageField(upload_to='profile_picture/%y%m%d',blank=True,null=True)
    age=models.IntegerField()