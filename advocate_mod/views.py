from django.shortcuts import render,redirect
from django.http import HttpResponse
from advocate_mod.models import*
from user_mod.models import*


# Create your views here.


def adreg(request):
    return render(request,"adregistration.html")
def registration(request):
    return render(request,"registration.html")
def create(request):
    if request.method=="POST":
        aname=request.POST['aname']
        gender=request.POST['gender']
        email=request.POST['email']
        phone_no=request.POST['phone_no']
        about=request.POST['about']
        image=request.FILES.get('image')
        advocate.objects.create(
            aname=aname,
            gender=gender,
            email=email,
            phone_no=phone_no,
            about=about,
            image=image 
          )
    return render(request,"registration.html")

def advolog(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        if advocate.objects.filter(email=email,password=password).exists():
            data = advocate.objects.filter(email=email, password=password).values('id','aname','email').first()
            request.session['aid'] = data['id']
            request.session['name'] = data['aname']
            request.session['email'] = data['email']
            return redirect("schedule")
        else:
            return HttpResponse("invalid details")
        
    return render(request,"advologin.html")

def schedule(request):
    name=request.session.get('name')
    s=appointment.objects.filter(ap_aname=name)
    context={
        'name':name,
        's':s
    }
    return render(request,"schedule.html",context)

def arrange(request,id):
    appointment.objects.filter(id=id).update(
        appointment="scheduled"
    )
    return redirect("schedule")

def cancel(request,id):
    appointment.objects.filter(id=id).update(
        appointment="canceled"
    )
    return redirect(schedule)

def show(request):
    name=request.session.get('name')
    show=appointment.objects.filter(ap_aname=name)
    context={
        'show':show
    }
    return render(request,"myappointments.html",context)



