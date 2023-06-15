from django.urls import path
from . import views

urlpatterns = [
    path('', views.getStarted, name='login'),  # Update the URL pattern name to 'home'
    path('about', views.aboutUs, name='about'),
    path('blogs', views.blogs, name='blogs'),
    path('contact', views.contactUs, name='contact'),
    path('signup', views.signUp, name='signup'),
    path('newacc', views.newacc, name='newacc'),
    path('login', views.login_view, name='auth-login'),
    path('logout', views.logout_page, name='logout'),
    path('success', views.success_view, name='success'),
    path('home', views.default, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
]
