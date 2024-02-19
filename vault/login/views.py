# FOR REST_FRAMEWORK_TOKEN

from django.contrib import messages
from django.http import HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import render, redirect
from .models import userlogin

@csrf_exempt
def Login(request):
    if request.method == "GET":
        return render(request, 'Login_1.html')


from django.contrib.auth import authenticate
@csrf_exempt
def loguser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = authenticate(username=username, password=password)
            userparam = userlogin.objects.get(username=username)
            print("useruseruser", user)
            if userparam:
                user_details = {
                    'username': userparam.username,
                    'id': userparam.id,
                    'Role': userparam.Role,
                }

                refresh_token = RefreshToken.for_user(userparam)
                access_token = refresh_token.access_token

                access_token.payload.update(user_details)
                print("access_token:", access_token)
                print("refresh_token:", refresh_token)

                firstname = userparam.firstname
                lastname = userparam.lastname
                messages.success(request, f"Successfully Login [ {firstname} {lastname} ]")
                return render(request, 'Homepage_3.html', {"access_token": access_token, "refresh_token": refresh_token, "data": user})

        except userlogin.DoesNotExist:
            messages.error(request, "Invalid Username Password")



#:::::::::::::::::::::::::::::::::::: COMMENT :::::::::::::::::::::::::::::::::::::

#!!!!!!!!!!!!!!!!!!!!!! IMPORTANT   YOU WILL USE THE GET FUNCTION INSTEED THIS
# return render(request, 'Login')  IF YOU WANT TO SEND THE RETURN RESPONSE HERE WE MENTION NEEDED.
# ITS NOT IMPORTANT FOR FIRST TIME THIS FUNCTION RENDERING

# def Logout(request):
    # try:
    #     user = userlogin.objects.get(firstname = firstname, lastname = lastname)
    # userloginserializer = {
    #     firstname : userloginserializer.firstname
    #     lastname : userloginserializer.lastname
    # }
    # return render(request, "Login.html")

#:::::::::::::::::::::::::::::::::::: COMMENT :::::::::::::::::::::::::::::::::::::


@csrf_exempt
def Forgot(request):
    if request.method == "GET":
        return render(request, 'Password_Reset_2.html')

    if request.method == "DELETE":
        return render(request, 'Password_Reset_2.html')

    if request.method == "POST":
        username = request.POST.get("username")
        newpassword = request.POST.get("newpassword")
        retypepassword = request.POST.get("retypepassword")
        try:
           user = userlogin.objects.get(username=username)
           if user:
               check = newpassword == retypepassword
               if check:
                   user.password = retypepassword
                   user.save()
                   firstname = user.firstname
                   lastname = user.lastname
                   messages.success(request, f"Password Reset Done for [ {firstname} {lastname} ]")
                   return redirect('Login')

               else:
                   messages.error(request, "Password doesn't Match")
                   return render(request, 'Password_Reset_2.html', {'error': 'Passwords do not match'})

        except userlogin.DoesNotExist:
            messages.error(request, "User does not Exist")
            return render(request, 'Password_Reset.html', {'error': 'User does not exist'})

    return render(request, 'Password_Reset_2.html')

def Logout(request):
    return redirect("Login")