from django.contrib import admin

# Register your models here.
from api_apps.models import student, Teacher


@admin.register(student)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'f_name', 'l_name']



@admin.register(Teacher)
class Teacher(admin.ModelAdmin):
    list_display = ['id', 'f_name', 'l_name','email']
