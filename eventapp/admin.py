from django.contrib import admin
from . models import *
# Register your models here.

admin.site.register(Event)
admin.site.register(EventDate)
admin.site.register(Time)
admin.site.register(EventSlot)