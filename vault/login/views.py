# FOR REST_FRAMEWORK_TOKEN

from django.contrib import messages
from django.http import HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import render, redirect
from .models import userlogin
from django.contrib.auth import authenticate, login, logout


@csrf_exempt
def Login(request):
    if request.method == "GET":
        return render(request, 'Login_1.html')



@csrf_exempt
def loguser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username)
        print(password)
        try:
            user = userlogin.objects.get(username=username, password=password)
            if user:
                userparam = userlogin.objects.get(username=username)
                print("useruseruser", user)
                if userparam:
                    user_details = {
                        'username': userparam.username,
                        'id': userparam.id,
                        'Role': userparam.Role,
                    }

                    request.session['cookieToken'] = userparam.username, userparam.id, userparam.Role

                    refresh_token = RefreshToken.for_user(userparam)
                    access_token = refresh_token.access_token

                    access_token.payload.update(user_details)
                    print("access_token:", access_token)
                    print("refresh_token:", refresh_token)

                    firstname = userparam.firstname
                    lastname = userparam.lastname
                    messages.success(request, f"Successfully Login [ {firstname} {lastname} ]")
                    # return render(request, 'Homepage_3.html', {"access_token": access_token, "refresh_token": refresh_token, "data": user})
                    return redirect('Userhomepage')

            else:
                messages.error(request, "Please SIGNIN for LOGIN")

        except:
            messages.error(request, "Invalid Username or Password")
            return render(request, 'Login_1.html')



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

#:::::::::::::::::::::::::::::::::::: COMMENT ::::::::::::::::::::::::::::::::::::::



@csrf_exempt
def Forgot(request):
    if request.method == "POST":
        otp = request.POST.get("otp")
        newpassword = request.POST.get("newpassword")
        retypepassword = request.POST.get("retypepassword")
        try:
           user = emailotp.objects.get(otp=otp)
           if user.email:
               if newpassword == retypepassword:
                   print("IF++++++++++++++++++++++++++++++++++++++++++++++++")
                   login_user = userlogin.objects.get(username=user.email)
                   login_user.password = retypepassword
                   login_user.save()
                   firstname = login_user.firstname
                   lastname = login_user.lastname
                   messages.success(request, f"Password Reset Done for [ {firstname} {lastname} ]")
                   return redirect('Login')

               else:
                   print("ELSE++++++++++++++++++++++++++++++++++++++++++++++++")
                   messages.error(request, "Newpassword and Rertyepassword Should be Same")
                   return redirect("Forgotpassword")

        except userlogin.DoesNotExist:
            print("EXCEPT++++++++++++++++++++++++++++++++++++++++++++++++")
            messages.error(request, "Invalid OTP")
            return redirect("Forgotpassword")

    return render(request, 'Password_Reset_2.html')



import random
from .models import emailotp
def otp_gen(request):
    if request.method == "POST":
        username = request.POST.get("username")
        if username:
            print("Forgot_Request_Username======================>", username)
            try:
                user = userlogin.objects.get(username=username)
                print("user------------------------------------->", user)
                if user:
                    random_integer = random.randint(1000, 9999)
                    print("random_integer========================>", random_integer)
                    try:
                        otp_user = emailotp.objects.get(email=username)
                        print("otp_user===========================>", otp_user)
                        if otp_user:
                            otp_user.otp = random_integer
                            otp_user.save()
                            otp = otp_user.otp
                            messages.success(request, f"YOUR OTP IS {otp}")
                            return render(request, "Password_Reset_3.html")

                    except:
                        print("Except_Block==========================>")
                        otp_user = emailotp.objects.create(email=username, otp=random_integer)
                        else_otp = otp_user.otp
                        messages.success(request, f"YOUR OTP IS {else_otp}")
                        return render(request, "Password_Reset_3.html")

            except:
                messages.error(request, "User Not Found")

        else:
            messages.error(request, "Please Provide the Valid Username")
            return redirect("Forgotpassword")

    if request.method == "GET":
        return render(request, "404Errorpage.html")



def Logout(request):
    logout(request)
    return redirect('Login')