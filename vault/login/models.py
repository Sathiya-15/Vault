from django.db import models
from datetime import datetime


# def filepath(filename):
#     return os.path.join('userimages/', filename)

class userlogin(models.Model):
    username = models.EmailField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    firstname = models.CharField(max_length=100, null=True, blank=True)
    lastname = models.CharField(max_length=100, null=True, blank=True)
    mobilenumber = models.BigIntegerField(null=True, blank=True)
    Background_image = models.ImageField(upload_to='userimages/', null=True, blank=True,default='userimages/default_back.png')
    Profile_image = models.ImageField(upload_to='userimages/', null=True, blank=True,default='userimages/default_profile.png')
    created_at = models.DateTimeField(default=datetime.now(), blank=True, null=True)
    address = models.CharField(max_length=225, null=True,blank=True)
    city = models.CharField(max_length=225, null=True,blank=True)
    country = models.CharField(max_length=225, null=True,blank=True)
    pincode = models.BigIntegerField(null=True,blank=True)
    aboutme = models.CharField(max_length=225, null=True,blank=True)
    Role = models.CharField(max_length=225,null=True,blank=True)

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