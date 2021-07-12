from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('registerPage/',views.registerPage,name='registerPage'),
    path('loginPage/',views.loginPage,name='loginPage'),
    path('logoutUser/',views.logoutUser,name='logoutUser'),
    path('profile',views.profile,name='profile'),
    path('user/createProfile/',views.createProfile,name='createProfile'),

    path('courses/',views.courses,name='courses'),

]
