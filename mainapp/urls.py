from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('userLogin', views.userLogin, name='userLogin'),
    path('userSignup', views.userSignup, name='userSignup'),
    path('userLogout', views.userLogout, name='userLogout'),
]
