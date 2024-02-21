from django.urls import path
from advocate_mod import views

urlpatterns = [
    
    path('adreg',views.adreg,name="adreg"),
    path('reg',views.registration,name="registration"),
    path('create',views.create,name="create"),
    path('advolog',views.advolog,name="advolog"),
    path('schedule',views.schedule,name="schedule"),
    path('arrange/<int:id>',views.arrange,name="arrange"),
    path('cancel/<int:id>',views.cancel,name="cancel"),
    path('my',views.show,name="my")
]