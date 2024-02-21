from django.contrib import admin
from advocate_mod.models import*
from user_mod.models import*
# Register your models here.
admin.site.register(advocate)
admin.site.register(user)
admin.site.register(appointment)
