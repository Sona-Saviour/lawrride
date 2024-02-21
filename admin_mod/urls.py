from django.urls import path
from admin_mod import views

urlpatterns = [

    path('',views.home,name="home"),
    path('adm1',views.admin1,name="admin1"),
    path('adm',views.admin,name="adm"),
    path('tab',views.tab,name="tab"),
    path('read',views.read,name="read"),
    # path('accept/<int:id>',views.accept,name="accept"),
    path('approve/<int:id>',views.approve,name="approve"),
    path('reject/<int:id>',views.reject,name="reject"),
    path('re',views.re,name="re"),
    path('user',views.use,name="user"),
    path('edit/<int:id>',views.edit,name="edit"),
    path('update/<int:id>',views.update,name="update"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('ser',views.ser,name="ser"),
    path('about',views.about,name="about"),
    path('apptab',views.apptab,name="apptab"),
    path('complaint',views.compl,name="complaint"),
    path('comtable',views.ctable,name="comtable"),
    path('complainttable',views.comptab,name="complainttable"),
    path('admlog',views.admlog,name="admlog")
]