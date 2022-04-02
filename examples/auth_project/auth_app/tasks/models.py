from django.db import models
from my_auth.models import MyUser


class TaskStatuses(models.Model):
    name = models.CharField(max_length=32, default="")


class Task(models.Model):
    name = models.CharField(max_length=32, default="")
    creator = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="+")
    date_create = models.DateTimeField(auto_now_add=True)
    worker = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="+")
    status = models.ForeignKey(TaskStatuses, on_delete=models.CASCADE)


class TaskComments(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="+")
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=255, default="")
