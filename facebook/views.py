

from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.db import IntegrityError
from facebook.models import users
from facebook.models import wallpost
from facebook.models import frequests
from facebook.models import Player_Profile
import os


def login(request):
    return render(request,"login.html")

def save(request):
    s = users()
    s.Email_id = request.GET.get("Email_id")
    s.password = request.GET.get("password")
    s.username = request.GET.get("username")
    s.ph_no = int(request.GET.get("ph_no"))
    s.gender = request.GET.get("gender")
    s.save()
    return render(request,"welcome.html")

def log_in(request):
   u=users.objects.filter(Email_id=request.GET.get('Email_id'),password=request.GET.get('password'))
   if u.exists()==True:
       request.session['Email_id']=request.GET.get('Email_id')
       res=redirect("welcome")
       return res
   else:
       return render(request,"login.html")

def welcome(request):
    f=frequests.objects.filter(reciever=request.session.get('Email_id'),status=0)
    wpost=wallpost.objects.all()
    return render(request, "welcome.html",{"request":f,"wposts":wpost})


def requestsend(request):
    f=frequests()
    f.sender=request.session.get("Email_id")
    f.reciever=request.GET.get("rec")
    f.status=0
    f.save()
    return redirect("welcome")
def requestaccept(request):
    f=frequests.objects.get(rid=request.GET.get('rid'))
    f.status=1
    f.save()
    return redirect('welcome')
def requestreject(request):
    f=frequests.objects.get(rid=request.GET.get('rid'))
    f.status=2
    f.save()
    return redirect('welcome')



def sendmsg(request):
    m=wallpost()
    m.sender=request.GET.get("id")
    m.message=request.GET.get("msg")
    m.save()
    return redirect('welcome')
def index(request):
    pp=Player_Profile.objects.all()
    return render(request,"index.html",{"users":pp})
def uploadpic(request):
    try:
       if request.method=='POST':
            username=request.POST.get('username')
            email=request.POST.get('email')
            age=request.POST.get('age')
            pic=request.FILES.get('myfile')
            profile_obj=Player_Profile(profile_picture=pic,name=username,email=email,age=age).save()
            return redirect("index")
    except Exception as e:
        return HttpResponse(e)
