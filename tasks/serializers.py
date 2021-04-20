from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework.serializers import HyperlinkedModelSerializer

from tasks.models import Task


class TaskSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"  # ('url', 'title', '')
