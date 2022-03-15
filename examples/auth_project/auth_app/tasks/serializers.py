from rest_framework import serializers
from .models import Task, TaskStatuses, TaskComments


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "name", "creator", "date_create", "worker", "status"]


class TaskStatusesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskStatuses
        fields = ["id", "name"]


class TaskCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskComments
        fields = ["id", "user", "task", "date", "text"]
