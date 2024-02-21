from django.urls import path
from user_mod import views

urlpatterns = [
    path('register',views.register,name="register"),
    path('display',views.display,name="display"),
    path('pro/<int:id>',views.profile,name="pro"),
    path('app/<int:id>',views.appoint,name="app"),
    path('userlog',views.userlog,name="userlog"),
    path('booking/<int:id>',views.booking,name="booking"),
    path('userbook',views.userbook,name="userbook")
 ]