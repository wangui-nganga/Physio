
# Register your models here.
from django.contrib import admin
from .models import  Appointment, Service

admin.site.register(Appointment)
admin.site.register(Service)
