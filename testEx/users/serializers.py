from rest_framework import serializers
from django.contrib.auth import get_user_model
from phonenumber_field import serializerfields

from .models import Employee, Customer
from .utils import UserSerializerMixin


class EmployeeSerializer(UserSerializerMixin):
    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = Employee.objects.create_user(**validated_data)
        return user


class CustomerSerializer(UserSerializerMixin):
    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = Customer.objects.create_user(**validated_data)
        return user