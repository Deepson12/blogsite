from django.urls import path
from . import views


urlpatterns=[
    path('', views.blogHome, name='home'),
    path('getstarted', views.getStarted, name='login'),
    path('signup', views.signUp, name='signup'),
    path('blogs', views.blogs, name='blogs'),
    path('contact', views.contactUs, name='contact'),
    path('about', views.aboutUs, name='about'),
]