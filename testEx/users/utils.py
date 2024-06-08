from phonenumber_field import serializerfields
from rest_framework import status, serializers
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .models import CustomUser


class UserCreateionAPIMixin(CreateAPIView):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response({
            "user": serializer.data,
            "message": f"{self.user_type} created successfully",
        }, status=status.HTTP_201_CREATED, headers=headers)


class UserSerializerMixin(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=150)
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    phone = serializerfields.PhoneNumberField()

    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'password_confirm', 'phone', 'user_type')

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("Passwords do not match")
        return data
