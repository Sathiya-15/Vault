from django.db import models
import os
from django.utils import timezone


# def filepath(filename):
#     return os.path.join('userimages/', filename)

class userlogin(models.Model):
    username = models.EmailField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    firstname = models.CharField(max_length=100, null=True, blank=True)
    lastname = models.CharField(max_length=100, null=True, blank=True)
    mobilenumber = models.BigIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='userimages/', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True, null=True)

# class emailotp(models.Model):
#     email = models.EmailField(max_length=100, null=True, blank=True)
#     otp = models.CharField(max_length=6, null=True, blank=True)

# class userdocuments(models.Model):
#     pdf = models.FileField(upload_to='pdf/', null=True, blank=True)
#     image = models.ImageField(upload_to='image/', null=True, blank=True)

# def constr(request,images):
#     data = userlogin.objects.get(images=images)
#     filepath = "file:///home/vasanth/PycharmProjects/Project/vault/" + data
#     return(constr)