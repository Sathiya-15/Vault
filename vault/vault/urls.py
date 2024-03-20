"""
URL configuration for vault project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from user import views as user_views
from login import views as login_view


from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path("Logout/", login_view.Logout, name="Logout"),
    path("Admin/", admin.site.urls),
    path("", login_view.Login, name="Login"),
    path("LoggedInUser/", login_view.loguser, name="LoggedInUser"),
    path("DeleteUser/<str:id>/", user_views.Deleteuser, name="Delete_User"),
    path("MyProfile/", user_views.Profile_View, name="Myprofile"),
    path("ProfileUpdate/", user_views.profileupdate, name="profileupdate"),
    path("NewAccountCreation/", user_views.Createnewaccount, name="Createnewaccount"),
    path("ForgotPassword/", login_view.Forgot, name='Forgotpassword'),
    path("MyDashBoard/", user_views.Mydashboard, name="Userhomepage"),
    path("Users_Table_View/", user_views.Users, name="Table_Users"),
    path("CreateUser/", user_views.createuser, name="createuser"),
    path("UpdateUser/", user_views.Updateuser, name="Update_User"),
    path("UserView/<str:id>/", user_views.list_profile, name="list_profile"),
    path("Attendence/", user_views.attendence, name="attendence"),
    path("books/", user_views.books, name="books"),
    path("Search_Box/", user_views.search_box, name="search_box"),
    path("clear_search/", user_views.clear_search, name="clear_search"),
    path("otp_gen/", login_view.otp_gen, name="otp_gen"),
    path("pdf_view/", user_views.pdf_export, name="pdf_export"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# from django.contrib import admin
# from django.urls import path
# from user.userviews import Homepage
# from user.userviews import Mydashboard
# from user.userviews import Myfiles
# from user.userviews import Createnewaccount
# from login.views import Login
# from login import views as login_view
#
# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("", Login, name="Login"),
#     path("Home/", Homepage, name='Home'),
#     path("MyFiles/", Myfiles, name="MyFiles"),
#     path("Newaccountcreation/", Createnewaccount, name="Createnewaccount"),
#     path("Forgotpassword/", login_view.Forgot, name='forgotpassword'),
#     path("Mydashboard/", Mydashboard, name="Userhomepage")
# ]