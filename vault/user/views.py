import jwt
from vault import settings
import urllib.parse
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from login.models import userlogin
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import HttpResponse
from django.core.paginator import Paginator
from rest_framework.response import Response
from login.serializer import userloginserializer




@csrf_exempt
def Createnewaccount(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
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

    return HttpResponse("Invalid request method")



def Updateuser(request):
    print("Request=======================>", request)
    Body = request.body
    print("Body==========================>", Body)
    headers = request.headers
    print("Headers=======================>", headers)
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




#::::::::::::::::::::::::::::::::::::USING SERIALIZERS YOU NEED CLASS METHOD:::::::::::::::::::::::::::::::::::::
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
#::::::::::::::::::::::::::::::::::::USING SERIALIZERS IF YOU WANT THIS USE CLASS METHOD::::::::::::::::::::::::



# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
def Profile_View(request):
    if request.method == "GET":
        cookieToken = request.session.get("cookieToken")
        print("cookieToken========================>", cookieToken)
        try:
            username, id, Role = cookieToken
            users = userlogin.objects.get(id=id)
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



def Mydashboard(request):
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

    return HttpResponse("Method not allowed")




# @api_view(['GET'])
# @login_required
@permission_classes([IsAuthenticated])
def Users(request):
    print("User authenticated:", request.user.is_authenticated)
    if request.method == "GET":
        headers = request.headers
        cookieToken = request.session.get("cookieToken")
        if cookieToken:
            print("cookieToken===================>", cookieToken)
            username, id, Role = cookieToken

            print("username_in_session===========>", username)
            print("Role_in_session===============>", Role)
            print("id_in_session=================>", id)

            print("request=======================>", request)
            print("request.user==================>", request.user)
            print("headers=======================>", headers)

            authorization_header = request.headers.get('Authorization')
            print("authorization_header===========>", authorization_header)

            # encoded_value = request.COOKIES.get('Vault_Cookie', '')
            # decoded_value = urllib.parse.unquote(encoded_value)
            # print("encoded_value:======================>", encoded_value)
            # print("decoded_value:======================>", decoded_value)

            try:
                if Role == 'Superadmin':
                    query_set = userlogin.objects.all().order_by('id')
                    total_value = query_set.count()
                    print("No_of_count====================>", total_value)
                    print("query_set======================>", query_set)
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
                    print("users_data:====================>", users_data)

                    items_perpage = 5
                    paginator = Paginator(users_data, items_perpage)

                    page_count = paginator.num_pages
                    print("PAGE_COUNT====================>", page_count)

                    page_number = request.GET.get("page", 1)
                    print("page_number=====================>", page_number)
                    page = paginator.get_page(page_number)
                    print("Page number:", page.number)
                    print("Items on this page:", page.object_list)


                    print("user_data:====================>", page)
                    return render(request, "Users_Table_View.html", {"admindata": page})


                elif Role == 'Teacher':
                    query_set = userlogin.objects.filter(Role__in=['Student', 'Student-Leader', 'Student-CO-Ordinator'])
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
                    print("user_data:====================>", user_data)
                    items_perpage = 5
                    paginator = Paginator(users_data, items_perpage)

                    page_count = paginator.num_pages
                    print("PAGE_COUNT====================>", page_count)

                    page_number = request.GET.get("page", 1)
                    print("page_number=====================>", page_number)
                    page = paginator.get_page(page_number)

                    print("Page number:", page.number)
                    print("Items on this page:", page.object_list)

                    print("user_data:====================>", page)
                    return render(request, "Users_Table_View.html", {"teacherdata": page})

                else:
                    messages.error(request, "No Data Found")
                    return render(request, "Users_Table_View.html")

            except userlogin.DoesNotExist:
                messages.error(request, "Users do not exist in the database.")
                return render(request, "Users_Table_View.html")

        else:
            return render(request, "404Errorpage.html")



# @login_required
def attendence(request):
    if request.method == "GET":
        return render(request, "Attendence.html")

    if request.method == "POST":
        log_in_at = request.POST.get("login_at")
        try:
            user = userlogin.objects.get(id=1)
            if user:
                attendance = attendence.objects.create(userlogin=user, log_in_at=log_in_at)
                print("attendance:=============>", attendance)
                return render(request, "Attendence.html", {"attendance": attendance})
        except:
            messages.error(request, "User Not Found")
            return render(request, "Attendence.html")



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
            userlogin.objects.create(username=username, firstname=firstname, lastname=lastname, mobilenumber=mobilenumber, Role=Role)
            messages.success(request, "User Added Successfully")
            return redirect("Table_Users")



def list_profile(request, id):
    print("id========>:", id)
    if request.method == "GET":
        try:
            user = userlogin.objects.get(username=id)
            return render(request, 'My_Profile2.html', {'data': user})

        except userlogin.DoesNotExist:
            messages.error(request, "No Data in Database")
            return render(request, 'My_Profile2.html')




def books(request):
    if request.method == "GET":
        return render(request, "Books.html")



def search_box(request):
    print("???????????????????????????????????????????", request)
    if request.method == "POST":
        username = request.POST.get("username")
        firstname = request.POST.get("username")
        lastname = request.POST.get("username")
        mobilenumber = request.POST.get("username")
        Role = request.POST.get("Role")
        print(username)
        print(firstname)
        print(lastname)
        print(mobilenumber)
        print(Role)
        user = userlogin.objects.filter(username=username, firstname=firstname, lastname=lastname, mobilenumber=mobilenumber, Role=Role)
        print(user)
        return render(request, "Users_Table_View.html", context=user)