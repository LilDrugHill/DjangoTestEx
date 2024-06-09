from rest_framework import permissions

from .models import Tasks
from users.models import CustomUser


class ItsMyTask(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.user_type == CustomUser.UserType.EMPLOYEE
        )

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.employee == request.user
