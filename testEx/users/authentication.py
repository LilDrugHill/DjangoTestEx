from rest_framework.authentication import BaseAuthentication
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User

from .models import CustomUser


class CookieAuthentication(BaseAuthentication):

    def authenticate(self, request):
        access_token = request.COOKIES.get("access_token")
        print(access_token)
        if not access_token:
            return None
        print(1)
        try:
            validated_token = AccessToken(access_token)
            print(validated_token["user_id"], 1)
            user = CustomUser.objects.get(id=validated_token["user_id"])
        except Exception as e:
            print(e)
            raise AuthenticationFailed("Invalid token")

        return (user, None)
