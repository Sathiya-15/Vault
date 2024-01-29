from django.contrib import messages
from django.shortcuts import render, redirect
from login.models import userlogin
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.template import loader
from django.http import HttpResponse
from rest_framework.response import Response
from login.serializer import userloginserializer




@csrf_exempt
def Createnewaccount(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        mobilenumber = request.POST.get("mobilenumber")
        username = request.POST.get("username")
        password = request.POST.get("password")
        retypepassword = request.POST.get("retypepassword")
        imageUpload = request.FILES.get("imageUpload")
        try:
            user = userlogin.objects.get(Q(username=username) | Q(mobilenumber=mobilenumber))
            if user:
                messages.error(request, "User Already Exist...! Kindly Login")
                return redirect('Login')

        except userlogin.DoesNotExist:
            if password == retypepassword:
                userlogin.objects.create(username=username, password=password,
                                         firstname=firstname, lastname=lastname,
                                         mobilenumber=mobilenumber,image=imageUpload)
                messages.success(request, "User Registered Successfully")
                return redirect('Login')
            else:
                messages.error(request, "Password and Retypepassword Should be Same")

    if request.method == "GET":
        return render(request, 'Createnewaccount.html')

    if request.method == "DELETE":
        return render(request, 'Createnewaccount.html')

    return render(request, 'Createnewaccount.html')


@csrf_exempt
def Deleteuser(request):
    if request.method == "GET":
        return render(request, 'deleteuser.html')

    if request.method == "POST":
       username = request.POST.get("username")
       try:
           user = userlogin.objects.get(username=username)
           if user:
               user.delete()
               messages.success(request, "User Database Deleted Successfully")
               return redirect('deleteuser')

       except userlogin.DoesNotExist:
           messages.error(request, "User Doesnot Exist")
           return render(request, 'deleteuser.html')



#::::::::::::::::::::::::::::::::::::USING SERIALIZERS IF YOU WANT THIS USE CLASS METHOD:::::::::::::::::::::::::::::::::::::
#
# def Profile_View(request):
#     if request.method == "GET":
#         try:
#             users = userlogin.objects.all()
#             # user_serializer = userloginserializer(users, many=True)
#             for user in users:
#             #     first_user = users[0]
#                 firstname = user.firstname
#                 lastname = user.lastname
#                 print(user)
#             context = {
#                     "firstname": firstname,
#                     "lastname": lastname,
#                 }
#             # else:
#             #     context = {}
#             return render(request, 'myprofile.html', context)
#
#         except userlogin.DoesNotExist:
#             messages.error(request, "No Data in Database")
#             return render(request, 'myprofile.html')
#
#::::::::::::::::::::::::::::::::::::USING SERIALIZERS IF YOU WANT THIS USE CLASS METHOD:::::::::::::::::::::::::::::::::::::


def Profile_View(request):
    if request.method == "GET":
        try:
            users = userlogin.objects.get(id=1)
            # Initialize lists to store data for all users
            # firstnames = []
            # lastnames = []
            # mobilenumbers = []
            # passwords = []
            # usernames = []
            # images = []
            # print(firstnames)
            # print(lastnames)

            # for user in users:
            #     print(user)
            #     firstnames.append(user.firstname)
            #     lastnames.append(user.lastname)
            #     mobilenumbers.append(user.mobilenumber)
            #     passwords.append(user.password)
            #     usernames.append(user.username)
            #     images.append(user)

            # context = {
            #     "firstnames": firstnames,
            #     "lastnames": lastnames,
            #     "mobilenumbers": mobilenumbers,
            #     "passwords": passwords,
            #     "usernames": usernames,
            #     "images": images,
            # }
            # print(context)
            return render(request, 'myprofile.html', {'data':users})

        except userlogin.DoesNotExist:
            messages.error(request, "No Data in Database")
            return render(request, 'myprofile.html')

def Homepage(request):
    return render(request, 'Homepage.html')

def Myfiles(request):
    return render(request, 'Myfiles.html')

def Mydashboard(request):
    return render(request, 'Homepage.html')

def profileupdate(request):
    if request.method == "POST":
        username = request.POST.get("username")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        mobilenumber = request.POST.get("mobilenumber")
        password = request.POST.get("password")
        imageUpload = request.FILES.get("imageUpload")
        try:
            user = userlogin.objects.get(username=username)
            if user:
                user.username = username
                user.firstname = firstname
                user.lastname = lastname
                user.mobilenumber = mobilenumber
                user.password = password
                user.image = imageUpload
                user.save()
                messages.success(request, "User Updated")
                return render(request, "myprofile.html", {'data': user})

        except userlogin.DoesNotExist:
            messages.error(request, "User Does not Exist")
            return render(request, "myprofile.html")

    # Return a response for the case where request.method is not "POST"
    return HttpResponse("Method not allowed")