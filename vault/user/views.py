from django.contrib import messages
from django.shortcuts import render, redirect
from login.models import userlogin
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

@csrf_exempt
def Createnewaccount(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        mobilenumber = request.POST.get("mobilenumber")
        username = request.POST.get("username")
        password = request.POST.get("password")
        retypepassword = request.POST.get("retypepassword")
        try:
            user = userlogin.objects.get(Q(username=username) | Q(mobilenumber=mobilenumber))
            if user:
                messages.error(request, "User Already Exist...! Kindly Login")
                return redirect('Login')

        except userlogin.DoesNotExist:
            if password == retypepassword:
                userlogin.objects.create(username=username, password=password, firstname=firstname, lastname=lastname, mobilenumber=mobilenumber)
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

    if request.method == "GET":
        return render(request, 'deleteuser.html')

    return render(request, 'deleteuser.html')

def Profile_View(request,pk):
        try:
            user = userlogin.objects.all()

        except userlogin.DoesNotExist:
            return render(request, 'myprofile.html', 'No Profile Found')

        return render(request, 'myprofile.html', {'obj': user})

def Homepage(request):
    return render(request, 'Homepage.html')

def Myfiles(request):
    return render(request, 'Myfiles.html')

def Mydashboard(request):
    return render(request, 'Homepage.html')