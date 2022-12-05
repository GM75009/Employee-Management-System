from django.shortcuts import render, HttpResponse,redirect,HttpResponseRedirect
from django.contrib.auth.models import User
from .models import *

# Create your views here.

def guru(request):
    return render(request,'header.html')


def guru1(request):
    return render(request,'index.html')

def guru2(request):
    if request.method=='POST':
        x=request.POST.get("u")
        y=request.POST.get("p")
        z=request.POST.get("pc")
        o=User.objects.create_user(x,y,z)
        o.save()
    else:
        return render(request,'registration.html',context={})
    return render(request,'index.html',{})

def index(request):
    return render(request,'index.html')

def addemp(request):
    if request.method=="POST":
        x1=request.POST.get("n")
        y1=request.POST.get("e")
        z1=request.POST.get("em")
        a1=request.POST.get("d")
        b=EmployeeDetail.objects.create(name=x1,empcode=y1,empdept=z1,designations=a1)
        b.save()
    else:
        return render(request,'employeedetails.html',{})
    return HttpResponseRedirect('/index')


def addall(request):
    if request.method=="POST":
        x2=request.POST.get("n")
        z2=request.POST.get("t")
        a2=request.POST.get("p")
        c=Addall.objects.create(name=x2,Time=z2,Place=a2)
        c.save()
    else:
        return render(request,'dob.html',{})
    return HttpResponseRedirect('/index')

def emlist(request):
    a3=EmployeeDetail.objects.all()
    b3={'em':a3}
    return render(request,'list.html',b3)