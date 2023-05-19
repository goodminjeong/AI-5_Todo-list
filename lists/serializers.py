from rest_framework import serializers
from lists.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        exclude = ("user",)
        extra_kwargs = {
            'is_complete': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'completion_at': {'read_only': True},
        }
