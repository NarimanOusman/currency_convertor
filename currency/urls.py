
from django.urls import include, path

from currency import admin
from . import views


urlpatterns = [
   
     path('', views.index, name='Home'),
     path('dashboard/',views.dashboard,name='dashboard'),
     path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
     path('terms-of-service/', views.terms_of_service, name='terms_of_service'),
     path('contact/', views.contact, name='contact'),
]
