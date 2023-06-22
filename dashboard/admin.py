from django.contrib import admin

from dashboard.models import Patient, Files, Retsep

# Register your models here.


admin.site.register(Patient)
admin.site.register(Files)
admin.site.register(Retsep)
