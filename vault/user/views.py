from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from login.models import userlogin
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import HttpResponse
from rest_framework.response import Response
from login.serializer import userloginserializer




@csrf_exempt
def Createnewaccount(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        # lastname = request.POST.get("lastname")
        mobilenumber = request.POST.get("mobilenumber")
        username = request.POST.get("username")
        password = request.POST.get("password")
        retypepassword = request.POST.get("retypepassword")
        # imageUpload = request.FILES.get("imageUpload")
        try:
            user = userlogin.objects.get(Q(username=username) | Q(mobilenumber=mobilenumber))
            if user:
                messages.error(request, "User Already Exist...! Kindly Login")
                return redirect('Login')

        except userlogin.DoesNotExist:
            if password == retypepassword:
                userlogin.objects.create(username=username, password=password,
                                         firstname=firstname, mobilenumber=mobilenumber)
                messages.success(request, "User Registered Successfully")
                return redirect('Login')
            else:
                messages.error(request, "Password and Retypepassword Should be Same")

    if request.method == "GET":
        return render(request, 'Create_New_Account.html')

    if request.method == "DELETE":
        return render(request, 'Create_New_Account.html')

    return render(request, 'Create_New_Account.html')


# @csrf_exempt
# def Deleteuser(request, id):
#     print("=========>", id)
#     if request.method == "POST":
#         username = request.POST.get("id")
#         try:
#             user = userlogin.objects.get(username=username)
#             user.delete()
#             messages.success(request, "User Database Deleted Successfully")
#             return redirect('Table_Users')
#
#         except userlogin.DoesNotExist:
#             messages.error(request, "User Doesnot Exist")
#             return render(request, 'Table_Users.html')

@csrf_exempt
def Deleteuser(request, id):
    if request.method == "GET":
        try:
            user = get_object_or_404(userlogin, username=id)
            user.delete()
            messages.success(request, "User Database Deleted Successfully")
            return redirect('Table_Users')
        except userlogin.DoesNotExist:
            messages.error(request, "User Does Not Exist")
            return render(request, 'Table_Users.html')

    return HttpResponse("Invalid request method")  # Add a default response for other HTTP methods

def Updateuser(request):
    print("......", request)
    username = request.POST.get("username")
    firstname = request.POST.get("firstname")
    lastname = request.POST.get("lastname")
    mobilenumber = request.POST.get("mobilenumber")
    Role = request.POST.get("Role")
    print("========>", request)
    if request.method == "POST":
        try:
            user = userlogin.objects.get(username=username)
            user.username = username
            user.firstname = firstname
            user.lastname = lastname
            user.mobilenumber = mobilenumber
            user.Role = Role
            user.save()
            return redirect("Table_Users")

        except:
            messages.error(request, "User Not Found")
            return redirect("Table_Users")


# def Deleteuser(request, id):
#     print("=========>", id)
#     if request.method == "POST":
#         try:
#             user = get_object_or_404(userlogin, username=id)
#             user.delete()
#             messages.success(request, "User deleted successfully")
#             return HttpResponseRedirect(reverse('Table_Users'))
#
#         except userlogin.DoesNotExist:
#             messages.error(request, "User does not exist")
#             return render(request, 'Table_Users.html')
#     else:
#         return render(request, 'Table_Users.html')


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
            return render(request, 'My_Profile2.html', {'data': users})

        except userlogin.DoesNotExist:
            messages.error(request, "No Data in Database")
            return render(request, 'My_Profile2.html')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Mydashboard(request):
    print("Request=======>:", request)
    user_details = {
        'username': request.user.username,
        'id': request.user.id,
        'Role': request.user.Role,
    }
    return render(request, 'Homepage_3.html')

def profileupdate(request):
    if request.method == "POST":
        username = request.POST.get("username")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        mobilenumber = request.POST.get("mobilenumber")
        password = request.POST.get("password")
        Background_image = request.FILES.get("Background_image")
        Profile_image = request.FILES.get("Profile_image")
        address = request.POST.get("address")
        city = request.POST.get("city")
        country = request.POST.get("country")
        # pincode = request.POST.get("pincode")
        aboutme = request.POST.get("aboutme")
        try:
            user = userlogin.objects.get(username=username)
            if user:
                user.username = username
                user.firstname = firstname
                user.lastname = lastname
                user.password = password
                # user.Profile_image = Profile_image
                # user.Background_image = Background_image
                user.address = address
                user.city = city
                user.country = country
                user.mobilenumber = mobilenumber
                user.aboutme = aboutme
                user.save()
                messages.success(request, "User Updated")
                return redirect("Myprofile")

        except userlogin.DoesNotExist:
            messages.error(request, "User Does not Exist")
            return render(request, "My_Profile2.html")

    # Return a response for the case where request.method is not "POST"
    return HttpResponse("Method not allowed")


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
def Users(request):
    headers = request.headers
    print("headers=======>:", headers)
    authorization_header = request.headers.get('Authorization')
    print("authorization_header:========>",authorization_header)

    try:
        query_set = userlogin.objects.all()
        users_data = []

        for user in query_set:
            user_data = {
                'username': user.username,
                'firstname': user.firstname,
                'lastname': user.lastname,
                'mobilenumber': user.mobilenumber,
                'Role': user.Role,
            }
            users_data.append(user_data)
            print(user_data)

        return render(request, "Dash_Board_Users.html", {"admindata": users_data})

    except userlogin.DoesNotExist:
        messages.error(request, "Users do not exist in the database.")
        return render(request, 'Dash_Board_Users.html')


def createuser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        mobilenumber = request.POST.get("mobilenumber")
        Role = request.POST.get("Role")
        try:
            user = userlogin.objects.get(Q(username=username) | Q(mobilenumber=mobilenumber))
            if user:
                messages.error(request, "User Already Exist")
                return redirect("Table_Users")

        except:
            userlogin.objects.create(username=username,firstname=firstname,lastname=lastname,mobilenumber=mobilenumber,Role=Role)
            messages.success(request, "User Added Successfully")
            return redirect("Table_Users")

def list_profile(request,id):
    print("id========>:", id)
    if request.method == "GET":
        try:
            user = userlogin.objects.get(username=id)
            return render(request, 'My_Profile2.html', {'data': user})

        except userlogin.DoesNotExist:
            messages.error(request, "No Data in Database")
            return render(request, 'My_Profile2.html')