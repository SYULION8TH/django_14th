from .models import Todo
from rest_framework import serializers
serializers.ModelSerializer
class TodoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    todo = serializers.CharField()
    created_date = serializers.DateTimeField(read_only=True)
    due_date = serializers.DateTimeField()
    done = serializers.BooleanField()

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.todo=validated_data.get('todo', instance.todo)
        instance.content = validated_data.get('due_date', instance.due_date)
        instance.done = validated_data.get('done', instance.done)
        instance.save()
        return instance
