from django.contrib import admin
from .models import Task, TaskStatuses

# Register your models here.
admin.site.register(Task)
admin.site.register(TaskStatuses)
