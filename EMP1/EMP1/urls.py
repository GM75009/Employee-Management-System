"""EMP1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

from EMP.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('WELCOME TO EMP',guru,name='guru1'),
    path('registration',guru2,name='guru2'),
    path('index',index,name='index'),
    path('addemp',addemp,name='addemp'),
    path('addall',addall,name='addall'),
    path('list',emlist,name='list'),
]
