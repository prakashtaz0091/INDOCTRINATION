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
    path('course/',views.course2,name='course2'),
    path('course_detail/',views.course3,name='course3'),
    path('subject_detail/',views.subject_detail,name='subjectDetail'),
    path('live_tutors/',views.live_tutors,name='liveTutors'),
    path('blogPage/',views.blogPage,name='blogPage'),
    path('contact/',views.contact,name='contact'),
    path('signvideo/',views.signVideo,name='signVideo'),
    path('signimage/',views.signImage,name='signImage'),

]
