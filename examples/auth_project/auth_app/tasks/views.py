from rest_framework import viewsets
from .models import Task, TaskStatuses, TaskComments
from .serializers import TaskSerializer, TaskStatusesSerializer, TaskCommentsSerializer
from rest_framework import permissions


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    # permission_classes = [permissions.IsAuthenticated]


class TaskStatusesViewSet(viewsets.ModelViewSet):
    serializer_class = TaskStatusesSerializer
    queryset = TaskStatuses.objects.all()


class TaskCommentsViewSet(viewsets.ModelViewSet):
    serializer_class = TaskCommentsSerializer
    queryset = TaskComments.objects.all()
