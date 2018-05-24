from django.db import models
from accounts.models import *
from django.utils import timezone

# Create your models here.
class Information(models.Model):
    android_id = models.CharField(max_length=200)
    advertiser_name = models.CharField(max_length=200)
    video_count = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200) 
    time = models.DateTimeField(default=timezone.now)



class Information1(models.Model):
    user_id = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200) 
    time = models.DateTimeField(default=timezone.now)    
 

class Information2(models.Model):
    user_id = models.CharField(max_length=200)
    video_count = models.CharField(max_length=200)
    video_id = models.CharField(max_length=200)
    time = models.DateTimeField(default=timezone.now)


class Information3(models.Model):
    user_id = models.CharField(max_length=200)
    speed = models.CharField(max_length=200)
    video_frquency = models.CharField(max_length=200) 
    time = models.DateTimeField(default=timezone.now) 


class Sendtotab(models.Model):
    
    user_id = models.CharField(max_length=200)
    video_id1 = models.CharField(max_length=200)
    video_id2 = models.CharField(max_length=200)
    video_id3 = models.CharField(max_length=200)
    video_id4 = models.CharField(max_length=200)
    video_id5 = models.CharField(max_length=200)
    time = models.DateTimeField(default=timezone.now)
                
                