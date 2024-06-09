from rest_framework import serializers

from users.serializers import UserDataSerializer
from .models import Tasks


class TasksCreationSerializer(serializers.Serializer):
    customer = serializers.HiddenField(default=serializers.CurrentUserDefault())
    title = serializers.CharField(max_length=255)
    closed_at = serializers.DateTimeField()

    def create(self, validated_data):
        task = Tasks.objects.create(**validated_data)
        return task


class TasksListSerializer(serializers.Serializer):
    title = serializers.CharField()
    customer = UserDataSerializer()
    employee = UserDataSerializer()
    status_display = serializers.SerializerMethodField()

    created_at = serializers.DateTimeField()
    closed_at = serializers.DateTimeField()
    slug = serializers.SlugField()

    def get_status_display(self, obj):
        return obj.get_status_display()


class TasksGetSerializer(serializers.Serializer):
    slug = serializers.SlugField()
    employee = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status_display = serializers.SerializerMethodField()

    def get_status_display(self, obj):
        return obj.get_status_display()

    def update(self, instance, validated_data):
        instance.status = Tasks.TasksStatuses.IN_PROGRESS
        instance.employee = validated_data.get("employee", instance.employee)
        instance.save()
        return instance


class TaskDoneSerializer(serializers.Serializer):
    report = serializers.CharField()
    slug = serializers.SlugField()
    status_display = serializers.SerializerMethodField()

    def get_status_display(self, obj):
        return obj.get_status_display()

    def update(self, instance, validated_data):
        instance.status = Tasks.TasksStatuses.DONE
        instance.report = validated_data.get("report", instance.report)
        instance.save()
        return instance
