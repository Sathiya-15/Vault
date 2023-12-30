from django.db import models


class userlogin(models.Model):
    DoesNotExist = None
    objects = None
    username = models.EmailField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    firstname = models.CharField(max_length=100, null=True, blank=True)
    lastname = models.CharField(max_length=100, null=True, blank=True)
    mobilenumber = models.BigIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

# class emailotp(models.Model):
#     email = models.EmailField(max_length=100, null=True, blank=True)
#     otp = models.CharField(max_length=6, null=True, blank=True)

class userdocuments(models.Model):
    pdf = models.FileField(upload_to='pdf/', null=True, blank=True)
    image = models.ImageField(upload_to='image/', null=True, blank=True)
