from django.urls import path
from myapp.views import *


urlpatterns = [
    path("", index, name="home"),
    path("home/", homePage, name="index"),
    path("main/", mainPage),
    path("register/", register),
    path('showdata/', getStudentDetails),

    path('showuserdata/<int:id>/', showUserData, name="show-user-data"),
    path('delete/<int:id>/', deleteUserData, name='delete-user-data' ),
    path('update/<int:id>/', updateData, name='update-data')
]
