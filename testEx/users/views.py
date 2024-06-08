from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, AllowAny, IsAdminUser

from .models import Employee, Customer
from .serializers import CustomerSerializer, EmployeeSerializer
from .permissions import IsCustomer, IsEmployee
from .utils import UserCreateionAPIMixin
# Create your views here.


class CreateEmployee(UserCreateionAPIMixin):
    permission_classes = [IsEmployee]
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    user_type = 'Employee'


class CreateCustomer(UserCreateionAPIMixin):
    permission_classes = [IsEmployee]
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    user_type = 'Customer'


class GetEmployeesInfo(ListAPIView):
    permission_classes = [IsCustomer]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class GetCustomersInfo(ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer