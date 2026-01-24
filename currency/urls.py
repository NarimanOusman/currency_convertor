
from django.urls import include, path

from currency import admin
from . import views


urlpatterns = [
   
     path('', views.index, name='Home'),
     path('dashboard/',views.dashboard,name='dashboard'),
]
