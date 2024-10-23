from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.homepage, name=""),
    path('register', views.register, name="register"),
    path('my-login', views.my_login, name="my-login"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('About', views.about, name="About"),
    path('user-lougout', views.user_logout, name="user-logout"),


]




