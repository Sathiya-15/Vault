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
            print("USERS==========================>", users)
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
    if request.method == "GET":
        cookieToken = request.session.get("cookieToken")
        print(cookieToken)
        if cookieToken:
            return render(request, 'Homepage_3.html')

        else:
            return render(request, "404Errorpage.html")



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

                    page_number = request.GET.get("page")
                    print("page_number===================>", page_number)
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
                    print("page_number===================>", page_number)
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



def attendence(request):
    if request.method == "GET":
        cookieToken = request.session.get("cookieToken")
        if cookieToken:
            print("cookieToken====================>",cookieToken)
            username , id, Role = cookieToken
            query_set = userlogin.objects.get(id=id)
            image = query_set.Profile_image
            print(image)
            print("query_set======================>", query_set)
            # user_data = []
            # for data in query_set:
            #     user = {
            #         'username': data.username,
            #         'Profile_image': data.Profile_image,
            #     }
            #     user_data.append(user)
            return render(request, "Attendence.html", {"data": query_set})

        else:
            return render(request, "404Errorpage.html")

    if request.method == "POST":
        cookieToken = request.session.get("cookieToken")
        if cookieToken:
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

        else:
            return render(request, "404Errorpage.html")



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
    page_number = request.GET.get("page")
    print("REQUEST============================================>", request)
    if request.method == 'POST':
        headers = request.headers
        cookieToken = request.session.get("cookieToken")
        print("Headers================================>", headers)
        if cookieToken:
            username, id, Role = cookieToken
            if Role == "Superadmin":
                username = request.POST.get('username')
                firstname = request.POST.get('firstname')
                lastname = request.POST.get('lastname')
                mobilenumber = request.POST.get('mobilenumber')
                Role = request.POST.get('Role')

                Searched_List = {
                    'username': username,
                    'firstname': firstname,
                    'lastname': lastname,
                    'mobilenumber': mobilenumber,
                    'Role': Role,

                }

                searched_query = Q(username__icontains=username) & \
                               Q(firstname__icontains=firstname) & \
                               Q(lastname__icontains=lastname) & \
                               Q(mobilenumber__icontains=mobilenumber) & \
                               Q(Role__icontains=Role)

                print("searched_query================>", searched_query)

                is_empty_query = all(value == '' for field, value in searched_query.children)

                if is_empty_query:
                    print("++++++++++++++++++++++++++++++++++++++++++", is_empty_query)
                    return redirect("Table_Users")

                else:
                    searched_results = userlogin.objects.filter(searched_query)
                    if searched_results:
                        print("Search_Results================>", searched_results)
                        users_data = []

                        for data in searched_results:
                            user_data = {
                                'username': data.username,
                                'firstname': data.firstname,
                                'lastname': data.lastname,
                                'mobilenumber': data.mobilenumber,
                                'Role': data.Role,
                            }
                            users_data.append(user_data)

                        print("Search_Results================>", users_data)

                        items_perpage = 10
                        paginator = Paginator(users_data, items_perpage)

                        page_count = paginator.num_pages
                        print("PAGE_COUNT====================>", page_count)

                        page_number = request.GET.get("page")
                        print("page_number===================>", page_number)
                        page = paginator.get_page(page_number)
                        print("Page number:", page.number)
                        print("Items on this page:", page.object_list)

                        print("user_data:====================>", page)

                        return render(request, 'Users_Table_View.html', {'search_results_admindata': page , 'Searched_List':Searched_List })

                    else:
                        messages.error(request, "Given Combination Does Not Exist")
                        messages.error(request, "Please Provide the Correct Combination")
                        return redirect("Table_Users")


            elif Role == "Teacher":
                username = request.POST.get('username')
                firstname = request.POST.get('firstname')
                lastname = request.POST.get('lastname')
                mobilenumber = request.POST.get('mobilenumber')
                Role = request.POST.get('Role')

                Searched_List = {
                    'username': username,
                    'firstname': firstname,
                    'lastname': lastname,
                    'mobilenumber': mobilenumber,
                    'Role': Role,
                }

                searched_query = Q(username__icontains=username) & \
                                 Q(firstname__icontains=firstname) & \
                                 Q(lastname__icontains=lastname) & \
                                 Q(mobilenumber__icontains=mobilenumber) & \
                                 Q(Role__icontains=Role)

                print("searched_query================>", searched_query)

                printed_Statement = searched_query.children
                print("printed_Statement=============>", printed_Statement)

                is_empty_query = all(value == '' for field, value in searched_query.children)

                if is_empty_query:
                    print("+++++++++++++++++++++++++++++++++++++++++++++++", is_empty_query)
                    return redirect("Table_Users")

                else:
                    searched_results = userlogin.objects.filter(searched_query, Role__in=['Student', 'Student-Leader',
                                                                                          'Student-CO-Ordinator'])

                    if not searched_results:
                        messages.error(request, "Please Search the Value as Given")
                        return redirect("Table_Users")

                        # searched_results = userlogin.objects.filter(searched_query).userlogin.objects.filter(Role__in=['Student', 'Student-Leader', 'Student-CO-Ordinator'])

                    print("RAW_QUERY=====================>", searched_results.query)
                    print("Search_Results================>", searched_results)
                    users_data = []
                    for data in searched_results:
                        user_data = {
                            'username': data.username,
                            'firstname': data.firstname,
                            'lastname': data.lastname,
                            'mobilenumber': data.mobilenumber,
                            'Role': data.Role,
                        }
                        users_data.append(user_data)

                    print("Search_Results================>", users_data)

                    items_perpage = 10
                    paginator = Paginator(users_data, items_perpage)

                    page_count = paginator.num_pages
                    print("PAGE_COUNT====================>", page_count)

                    page_number = request.GET.get("page")
                    print("page_number===================>", page_number)
                    page = paginator.get_page(page_number)
                    print("Page number:", page.number)
                    print("Items on this page:", page.object_list)

                    print("user_data:====================>", page)

                    return render(request, 'Users_Table_View.html', {'search_results_teacher': page, 'Searched_List':Searched_List})

        else:
            return render(request, '404Errorpage.html')

    else:
        return render(request, "404Errorpage.html")



def clear_search(request):
    return redirect("Table_Users")



# from reportlab.pdfgen import canvas
# from django.http import FileResponse
# def pdf_export(request):
#     data_from_db = userlogin.objects.all().order_by('id')
#
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="data_table.pdf"'
#     p = canvas.Canvas(response)
#
#     table_width = 500
#     table_height = 300
#     row_height = 20
#     col_widths = [150, 110, 100, 100, 100]
#
#     x_start = 10
#     y_start = 750
#
#     page_width_start = 20
#     page_width_ends = 120
#
#     page_height_start = 700
#     page_height_ends = 3000
#
#     headers = ['username', 'firstname', 'lastname', 'mobilenumber', 'Role']
#     for col, header in enumerate(headers):
#         p.drawString(x_start + sum(col_widths[:col]), y_start, header)
#
#     for row, data_row in enumerate(data_from_db):
#         y_position = y_start - (row + 1) * row_height
#         for col, col_width in enumerate(col_widths):
#             col_value = str(getattr(data_row, headers[col].replace(' ', '')))
#             p.drawString(x_start + sum(col_widths[:col]), y_position, col_value[:col_width])
#
#     p.showPage()
#     p.save()
#
#     return response

from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle


def pdf_export(request):
    # Query data from the database
    data_from_db = userlogin.objects.all()

    # Create PDF response
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="data_table.pdf"'

    # Create a PDF document
    pdf_doc = SimpleDocTemplate(response, pagesize=letter)

    # Define data and table styles
    table_data = []
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ])

    # Add headers to table data
    headers = ['Username', 'First Name', 'Last Name', 'Mobile Number', 'Role']
    table_data.append(headers)

    # Add data from the database to table data
    for user in data_from_db:
        user_info = [user.username, user.firstname, user.lastname, user.mobilenumber, user.Role]
        table_data.append(user_info)

    # Create the table
    table = Table(table_data)

    # Apply table style
    table.setStyle(table_style)

    # Add table to the PDF document
    pdf_doc.build([table])

    return response


