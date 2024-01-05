"""
URL configuration for web_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
     path('loginDetails/', views.loginDetails, name='loginDetails'),
     path('signDetails/', views.signDetails, name='adminSign'),
     path('dashboardDetails/', views.dashboardDetails, name='dashboard'),

   
     path('estateRegistration/', views.estateRegistration, name='estateRegistration'),
     path('dashboardDetails/', views.dashboardDetails, name='dashboard'),
     path('rentalDashboard/', views.rentalDashboard, name='rentalDashboard'),
     path('about/', views.about, name='about'),
     path('rentaltypeDetail/', views.rentaltypeDetail, name='rentaltypeDetail'),

     
     
     path('update/<int:id>', views.update, name='update'),
     path('list/<id>', views.update, name='list'),
     path('add/', views.add, name='add'),
     path('list/', views.list, name='list'),
     path('list/<int:id>', views.delete, name='delete')
]
