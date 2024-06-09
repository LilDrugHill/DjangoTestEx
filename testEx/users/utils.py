from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response



class UserCreationAPIMixin(CreateAPIView):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save(user_type=self.user_type)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                "user": serializer.data,
                "message": f"{user.get_user_type_display()} created successfully",
            },
            status=status.HTTP_201_CREATED,
            headers=headers,
        )
