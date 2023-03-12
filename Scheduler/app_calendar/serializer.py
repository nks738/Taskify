from rest_framework import serializers

from .models import Books
from .models import UserInfo
from .models import TaskInfo


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskInfo
        fields = '__all__'
