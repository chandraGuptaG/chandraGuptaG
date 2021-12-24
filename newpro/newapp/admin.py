from django.contrib import admin

# Register your models here.

from .models import Task

class TaskAdmin(admin.ModelAdmin):
    List_display = ['title', 'completed']
admin.site.register(Task,TaskAdmin)