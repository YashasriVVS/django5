from django.http import HttpResponse
from django.shortcuts import render




def demofunction(request):
    return HttpResponse("PFSD SDP PROJECT")



def demofunction1 (request):
    return HttpResponse("KL University")

def demofunction2 (request):
    return HttpResponse("Hi Yashasri")

def homefunction(request):
    return render(request,"index.html")

def aboutfunction(request):
    return render(request,"about.html")

def contactfunction(request):
    return render(request,"contact.html")

def loginfunction(request):
    return render(request,"login.html")

