from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser


# def filepath(filename):
#     return os.path.join('userimages/', filename)

class userlogin(AbstractUser):
    username = models.EmailField(max_length=100, null=True, blank=True, unique=True)
    password = models.CharField(max_length=50, null=True, blank=True, default="Asdf@123")
    firstname = models.CharField(max_length=100, null=True, blank=True)
    lastname = models.CharField(max_length=100, null=True, blank=True)
    mobilenumber = models.BigIntegerField(null=True, blank=True)
    Background_image = models.ImageField(upload_to='userimages/', null=True, blank=True,default='userimages/default_back.png')
    Profile_image = models.ImageField(upload_to='userimages/', null=True, blank=True, default='userimages/default_profile.png')
    created_at = models.DateTimeField(default=datetime.now(), blank=True, null=True)
    address = models.CharField(max_length=225, null=True,blank=True)
    city = models.CharField(max_length=225, null=True,blank=True)
    country = models.CharField(max_length=225, null=True,blank=True)
    pincode = models.BigIntegerField(null=True,blank=True)
    aboutme = models.CharField(max_length=225, null=True,blank=True)
    Role = models.CharField(max_length=225, null=True,blank=True)
    email = None
    first_name = None
    last_name = None




class attendence(models.Model):
    userlogin = models.ForeignKey(userlogin, on_delete=models.CASCADE)
    log_in_at = models.TimeField(null=False, blank=False)
    log_out_at = models.TimeField(null=False, blank=False)

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