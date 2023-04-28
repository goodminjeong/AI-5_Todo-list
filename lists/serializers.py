from rest_framework import serializers
from lists.models import Todo


class CreateTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ("title", "is_complete", "completion_at")


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        exclude = ("user",)
