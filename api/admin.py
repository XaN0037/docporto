from django.contrib import admin

from api.models.news import *
from api.models.doctors import *
from api.models.contact import *

admin.site.register(Doctor)
admin.site.register(Contact)
admin.site.register(New)

