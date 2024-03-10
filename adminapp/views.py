from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from .models import Admin,Student,Faculty,Course
# Create your views here.
def adminhome(request):
    return render(request,'adminhome.html')

def logout(request):
    return render(request,'login.html')

def checkadminlogin(request):
    adminuname=request.POST["uname"]
    adminpwd=request.POST["pwd"]


    flag=Admin.objects.filter(Q(username=adminuname)&Q(username=adminpwd))
    print(flag)

    if flag:
        return render(request,"adminhome.html")
    else:
        return HttpResponse("Login Failed")

def viewstudents(request):
    students=Student.objects.all()
    return render(request,"viewstudents.html",{"studentdata":students})

def viewfaculty(request):
    faculty=Faculty.objects.all()
    return render(request,"viewfaculty.html",{"facultydata":faculty})

def viewcourses(request):
    courses = Course.objects.all()
    return render(request,"viewcourses.html",{"coursedata":courses})