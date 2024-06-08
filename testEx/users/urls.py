from django.urls import path
from .views import CreateEmployee, CreateCustomer, GetEmployeesInfo

urlpatterns = [
    path('employee/create', CreateEmployee.as_view()),
    path('employee/list', GetEmployeesInfo.as_view()),
    path('customer/create', CreateCustomer.as_view())
]