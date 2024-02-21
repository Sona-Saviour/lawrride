from django.shortcuts import render,redirect
from django.http import HttpResponse
from user_mod.models import *
from advocate_mod.models import *
from admin_mod import views

# Create your views here.
def register(request):
    if request.method=="POST":
        uname=request.POST['uname']
        uemail=request.POST['uemail']
        phone=request.POST['phone']
        password=request.POST['password']
        user.objects.create(
            uname=uname,
            uemail=uemail,
            phone=phone,
            password=password
          )
        return redirect(userlog)
    return render(request,"userreg.html")

def userlog(request):
    if request.method=="POST":
        uemail=request.POST['uemail']
        password=request.POST['password']
        if user.objects.filter(uemail=uemail,password=password).exists():
            data = user.objects.filter(uemail=uemail, password=password).values('id','uname','uemail','phone').first()
            request.session['uid'] = data['id']
            request.session['uname'] = data['uname']
            request.session['uemail'] = data['uemail']
            request.session['phone'] = data['phone']
            return redirect("userbook")

        else:
            return HttpResponse("invalid details")
    return render(request,"userlogin.html")


def display(request):
    dict=advocate.objects.filter(status="Approved")
    context={
        'dict':dict
    }
    return render(request,"dis.html",context)


def profile(request,id):
    d=advocate.objects.filter(id=id)
    context={
        'd':d
    }
    return render(request,"pro.html",context)

def appoint(request,id):
    ad=advocate.objects.filter(id=id)
    uname=request.session.get('uname')
    uemail=request.session.get('uemail')
    context={
        'uname':uname,
        'uemail':uemail,
        'ad':ad
    }  
    return render(request,"appointment.html",context)

def booking(request,id):
    if request.method=="POST":
        uid=request.session.get('uid')
        print("----------------------------------")
        print(uid)
        aid=advocate.objects.get(id=id)
        ap_name=request.POST['uname']
        ap_email=request.POST['uemail']
        ap_aname=request.POST['aname']
        date_time=request.POST.get('date_time')
        appointment.objects.create(
            uid=user.objects.get(id=uid),
            aid=aid,
            ap_name=ap_name,
            ap_email=ap_email,
            ap_aname=ap_aname,
            date_time=date_time
        )
        return redirect("home")
    return render(request,"appointment.html")

def userbook(request):
    uname=request.session.get('uname')
    b=appointment.objects.filter(ap_name=uname)
    context={
        'uname':uname,
        'b':b
    }
    return render(request,"bookings.html",context)

