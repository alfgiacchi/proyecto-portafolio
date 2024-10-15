from django.contrib import admin
from .models import Project
# Register your models here.
# es necesario para  ver los campos ocultos. Es una configuracion extendida para poder ver campos ocultos
class Projectadmin(admin.ModelAdmin):
   readonly_fields=('created', 'update') 

admin.site.register(Project, Projectadmin) 