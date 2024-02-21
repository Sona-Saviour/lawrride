from django.shortcuts import render,redirect
from django.http import HttpResponse
from advocate_mod.models import*
from user_mod.models import*
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def home(request):

    return render(request,"home.html")

def admin1(request):
    return render(request,"admin.html")

def admin(request):
    return render(request,"adm.html")
def tab(request):
    return render(request,"tab.html")
def read(request):
    disp=advocate.objects.all()
    context={
        'disp':disp
    }
    return render(request,"tab.html",context)
# def accept(request,id):
#     d=advocate.objects.filter(id=id)
#     context={
#         'd':d
#     }
#     return render(request,context)

def approve(request,id):
    
    advocate.objects.filter(id=id).update(
        status="Approved"
    )
    return redirect(read)


def reject(request,id):
    
    advocate.objects.filter(id=id).update(
        status="Rejected"
    )
    return redirect(read)


def re(request):
    di=advocate.objects.filter(status="Approved")
    context={
            'di':di
        }
    return render(request,"accept.html",context)

def use(request):
    d=user.objects.all()
    context={
        'd':d 
    }
    return render(request,"ur.html",context)

def edit(request,id):
    edit=advocate.objects.filter(id=id)
    context=  {
        'edit':edit
    }
    return render(request,"edit.html",context)

def update(request,id):
     if request.method=="POST":
        aname=request.POST['aname']
        gender=request.POST['gender']
        email=request.POST['email']
        phone_no=request.POST['phone_no']
        about=request.POST['about']
        try:
            image = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(image.name, image)
        except MultiValueDictKeyError:
            file = advocate.objects.get(id=id).image
        advocate.objects.filter(id=id).update(
            aname=aname,
            gender=gender,
            email=email,
            phone_no=phone_no,
            about=about,
            image=file
          )
        return redirect('re')
     return render(request,"edit.html")



def delete(request,id):
    advocate.objects.filter(id=id).delete()
    return redirect('re')


def ser(request):
    return render(request,"services.html")

def about(request):
    return render(request,"about.html")

def apptab(request):
    a=appointment.objects.all()
    context={
        'a':a
    }
    return render(request,"apptable.html",context)

def compl(request):
    uname=request.session.get('uname')
    uemail=request.session.get('uemail')
    context={
        'uname':uname,
        'uemail':uemail,
    }  
    return render(request,"complaint.html",context)

def ctable(request):
    if request.method=="POST":
        cname=request.POST['uname']
        cemail=request.POST['uemail']
        subject=request.POST['subject']
        message=request.POST['message']
        complaint.objects.create(
            cname=cname,
            cemail=cemail,
            subject=subject,
            message=message
        )
    return render(request,"complaint.html")

def comptab(request):
    c=complaint.objects.all()
    context={
        'c':c
    }
    return render(request,"comptable.html",context)

def admlog(request):
    if request.method=="POST":
        name=request.POST['name']
        password=request.POST['password']
        if name=="admin" and password=="123@@@":
            return redirect("adm")
        else:
            return HttpResponse("error")
    return render(request,"admlog.html")