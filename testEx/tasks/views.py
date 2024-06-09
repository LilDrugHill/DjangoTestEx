from django.db.models import Q
from django.http import Http404
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.permissions import IsEmployee, IsCustomer
from users.models import CustomUser
from .models import Tasks
from .serializers import (
    TasksCreationSerializer,
    TasksGetSerializer,
    TaskDoneSerializer,
    TasksListSerializer,
)
from .permissions import ItsMyTask

# Create your views here.


class TaskListView(ListAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.user_type == CustomUser.UserType.EMPLOYEE:
            if user.is_staff:
                return Tasks.objects.all()
            else:
                return Tasks.objects.filter(
                    Q(status=Tasks.TasksStatuses.PENDING) | Q(employee=user)
                )

        elif user.user_type == CustomUser.UserType.CUSTOMER:
            return Tasks.objects.filter(customer=user)

        return Tasks.objects.none()


class TaskCreationView(CreateAPIView):
    serializer_class = TasksCreationSerializer
    permission_classes = [IsCustomer]
    queryset = Tasks.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        task = serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                "task": serializer.data,
                "message": f"Task {task.title} created successfully",
            },
            status=status.HTTP_201_CREATED,
            headers=headers,
        )


class TaskInProgressView(UpdateAPIView):
    permission_classes = [IsEmployee]
    queryset = Tasks.objects.all()
    serializer_class = TasksGetSerializer

    def get_object(self):
        slug = self.request.data.get("slug")
        if not slug:
            raise ValidationError("Slug is required.")

        try:
            return Tasks.objects.filter(status=Tasks.TasksStatuses.PENDING).get(
                slug=slug
            )
        except Tasks.DoesNotExist:
            raise Http404(
                "No task found matching the query or this one already IN PROGRESS"
            )


class TaskDoneView(UpdateAPIView):
    permission_classes = [ItsMyTask]
    serializer_class = TaskDoneSerializer
    queryset = Tasks.objects.all()

    def get_object(self):
        slug = self.request.data.get("slug")
        if not slug:
            raise ValidationError("Slug is required.")

        try:
            return Tasks.objects.filter(status=Tasks.TasksStatuses.IN_PROGRESS).get(
                slug=slug
            )
        except Tasks.DoesNotExist:
            raise Http404(
                "No task found matching the query or this one NOT IN PROGRESS"
            )
