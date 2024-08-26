from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('home/',views.home, name='home'),
    path('about/',views.about, name='about'),
]