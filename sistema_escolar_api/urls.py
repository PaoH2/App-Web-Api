"""point_experts_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from sistema_escolar_api.views import bootstrap, evento
from sistema_escolar_api.views import users
from sistema_escolar_api.views import alumnos
from sistema_escolar_api.views import maestros
from sistema_escolar_api.views import auth

urlpatterns = [
    #Version
        path('bootstrap/version', bootstrap.VersionView.as_view()),
    #Create Admin
        path('admin/', users.AdminView.as_view()),
    #Admin Data
        path('lista-admins/', users.AdminAll.as_view()),
    #Edit Admin
        path('admins-edit/', users.AdminViewEdit.as_view()),

    #Create Alumnos
        path('alumnos/', alumnos.AlumnosView.as_view()),

    #Alumno Data
        path('lista-alumnos/', alumnos.AlumnosAll.as_view()),

        path('alumnos-edit/', alumnos.AlumnosViewEdit.as_view()),
    #Create Mestros 
        path('maestros/', maestros.MaestrosView.as_view()),
    #Maestro Data
        path('lista-maestros/', maestros.MaestrosAll.as_view()),
        
        path('maestros-edit/', maestros.MaestrosViewEdit.as_view(), name='maestros-edit'),

    #Login
        path('token/', auth.CustomAuthToken.as_view()),
    #Logout
        path('logout/', auth.Logout.as_view()),
        
        path('evento/', evento.EventoView.as_view()),
        path('lista-evento/', evento.EventoAll.as_view()),
        path('evento-edit/', evento.EventosViewEdit.as_view()),
]
