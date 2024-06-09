from rest_framework.permissions import BasePermission
from .models import CustomUser


class IsEmployee(BasePermission):
    """
    Custom permission to only allow employees to access the view.
    """

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.user_type == CustomUser.UserType.EMPLOYEE
        )


class IsCustomer(BasePermission):
    """
    Custom permission to only allow customers to access the view.
    """

    def has_permission(self, request, view):

        print(
            request.user
            and request.user.is_authenticated
            and request.user.user_type == CustomUser.UserType.CUSTOMER
        )
        return (
            request.user
            and request.user.is_authenticated
            and request.user.user_type == CustomUser.UserType.CUSTOMER
        )
