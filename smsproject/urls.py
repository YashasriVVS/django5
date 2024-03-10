"""
URL configuration for smsproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views. home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("demo",views.demofunction,name="demo"),
    path("demo1",views.demofunction1,name="demo1"),
    path("demo2",views.demofunction2,name="demo2"),
    path("",views.homefunction,name=""),
    path("contact",views.contactfunction,name="contact"),
    path("about",views.aboutfunction,name="about"),
    path("login",views.loginfunction,name="login"),


    path("",include("adminapp.urls")),


]
