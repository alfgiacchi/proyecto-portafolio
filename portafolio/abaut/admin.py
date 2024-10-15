from django.contrib import admin
from .models import Course, Skill
# Register your models here.
# es necesario para  ver los campos ocultosco. Es una configuracion extendida para poder ver campos ocultos

class Abautadmin(admin.ModelAdmin):
   readonly_fields=('created', 'update') 

admin.site.register([Course, Skill], Abautadmin) 
