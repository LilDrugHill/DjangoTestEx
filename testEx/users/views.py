from django.contrib.auth import authenticate
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import (
    AllowAny,
    IsAdminUser,
    IsAuthenticated,
)
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .authentication import CookieAuthentication
from .models import CustomUser
from .serializers import UserDataSerializer, UserLoginSerializer
from .permissions import IsCustomer, IsEmployee
from .utils import UserCreationAPIMixin

# Create your views here.


class UserLoginView(APIView):
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer
    authentication_classes = []

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        print(email, password)
        user = authenticate(request, email=email, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            response = Response(
                {"access_token": access_token, "refresh_token": refresh_token}
            )

            response.set_cookie(
                key="access_token",
                value=access_token,
                httponly=True,
                secure=True,
                samesite="Lax",
            )

            response.set_cookie(
                key="refresh_token",
                value=refresh_token,
                httponly=True,
                secure=True,
                samesite="Lax",
            )

            return response
        else:
            return Response({"error": "Invalid credentials"}, status=400)


class TokenRetrieveView(APIView):
    authentication_classes = [CookieAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()

    def get(self, request):

        refresh = RefreshToken.for_user(request.user)

        return Response(
            {"access_token": str(refresh.access_token), "refresh_token": str(refresh)}
        )


class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [CookieAuthentication]

    def get(self, request):
        response = Response({"message": "Tokens deleted successfully"})

        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")

        return response


class CreateEmployee(UserCreationAPIMixin):
    permission_classes = [IsEmployee]
    serializer_class = UserDataSerializer
    queryset = CustomUser.objects.all()
    user_type = CustomUser.UserType.EMPLOYEE


class CreateCustomer(UserCreationAPIMixin):
    permission_classes = [IsEmployee]
    serializer_class = UserDataSerializer
    queryset = CustomUser.customers.all()
    user_type = CustomUser.UserType.CUSTOMER


class GetEmployeesInfo(ListAPIView):
    permission_classes = [IsCustomer]
    queryset = CustomUser.employees.all()
    serializer_class = UserDataSerializer


class GetCustomersInfo(ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = CustomUser.customers.all()
    serializer_class = UserDataSerializer
