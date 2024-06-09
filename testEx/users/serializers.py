from rest_framework import serializers
from phonenumber_field import serializerfields

from .models import CustomUser


class UserDataSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=150)
    full_name = serializers.CharField(max_length=50)
    phone = serializerfields.PhoneNumberField()
    user_type = serializers.HiddenField(default=0)

    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)

    def validate(self, data):
        if data["password"] != data["password_confirm"]:
            raise serializers.ValidationError("Passwords do not match")

        if not data["photo"]:
            raise serializers.ValidationError("Employee photo is required.")

        return data

    def create(self, validated_data):
        validated_data.pop("password_confirm")
        print(validated_data)
        user = CustomUser.objects.create_user(**validated_data)
        return user

    class Meta:
        model = CustomUser
        fields = ['photo']


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        if not data["password"] or not data["email"]:
            raise serializers.ValidationError("?")
        return data
