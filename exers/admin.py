from django.contrib import admin

# Register your models here.
from .models import *
class ExerAdmin(admin.ModelAdmin):
    list_display = ['name','likes','user','speciality','solution','subject','ex_file','date']
admin.site.register(Exer,ExerAdmin)
admin.site.register(Subject)
admin.site.register(Speciality)