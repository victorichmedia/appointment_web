from django.contrib import admin
from .models import Appointment, User

# Register your models here.
admin.site.register(User)
admin.site.register(Appointment)
