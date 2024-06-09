from django.urls import path
from .views import (
    CreateEmployee,
    CreateCustomer,
    GetEmployeesInfo,
    UserLoginView,
    UserLogoutView,
    TokenRetrieveView,
)

urlpatterns = [
    path("employee/create", CreateEmployee.as_view()),
    path("employee/list", GetEmployeesInfo.as_view()),
    path("customer/create", CreateCustomer.as_view()),
    path("login/", UserLoginView.as_view()),
    path("logout/", UserLogoutView.as_view()),
    path("refresh_token/", TokenRetrieveView.as_view()),
]
