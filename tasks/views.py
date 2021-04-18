from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from tasks.serializers import TaskSerializer
from tasks.models import Task
class TaskViewSet(ModelViewSet):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
    permission_classes = [AllowAny]
