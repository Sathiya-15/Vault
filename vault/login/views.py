# FOR GENERAL IMPORT

from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import userlogin
from django.http import HttpResponseNotAllowed



# FOR REST_FRAMEWORK_TOKEN

from django.conf import settings
from rest_framework_simplejwt.tokens import AccessToken
from vault.settings import SECRET_KEY
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import timedelta
from rest_framework.response import Response


@csrf_exempt
def Login(request):
    allowed_methods = ["GET", "POST"]

    if request.method == "GET":
        return render(request, 'Login.html')

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = userlogin.objects.get(username=username, password=password)
            if user:
                custom_payload ={
                    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
                    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
                    'ALGORITHM': 'HS256',
                    'SIGNING_KEY': SECRET_KEY,
                    'USERNAME': user.username,
                    'id': user.id,
                }
                refresh = RefreshToken.for_user(user)
                access_token = refresh.access_token
                print(access_token)

                custom_access_token = RefreshToken(refresh.get('token'))
                print("!!!!!!!!!!!!", custom_access_token)

                # access_token_payload = access_token.__dict__.get('_payload')
                # if access_token_payload:
                #     access_token.payload.update(custom_payload)
                #     print("!!!!!!!!!!!!", access_token.payload.update(custom_payload))

                firstname = user.firstname
                lastname = user.lastname
                messages.success(request, f"Successfully Login [ {firstname} {lastname} ]")
                return render(request, 'Homepage.html', {"data": custom_access_token})

        except userlogin.DoesNotExist:
            messages.error(request, "Invalid Username Password")
            return render(request, 'Login.html')

    return HttpResponseNotAllowed(allowed_methods)


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
        return render(request, 'Password_Reset.html')

    if request.method == "DELETE":
        return render(request, 'Password_Reset.html')

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
                   return render(request, 'Password_Reset.html', {'error': 'Passwords do not match'})

        except userlogin.DoesNotExist:
            messages.error(request, "User does not Exist")
            return render(request, 'Password_Reset.html', {'error': 'User does not exist'})

    return render(request, 'Password_Reset.html')