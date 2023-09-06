from django.contrib.auth import login, authenticate
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED
from ..validations import validate_email, validate_password
from ..serializers import UserLoginSerializer


class UserLoginView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny,)
    authentication_classes = (SessionAuthentication,)

    def post(self, request):
        data = request.data
        assert validate_email(data)
        assert validate_password(data)

        serializer = self.serializer_class(data=data)
        valid = serializer.is_valid()

        if valid:
            user = authenticate(email=data["email"], password=data["password"])
            if user:
                login(request, user)

            status_code = HTTP_200_OK
            response = {
                "success": True,
                "message": "User login successful",
                "access": serializer.data["access"],
                "refresh": serializer.data["refresh"],
                "authenticated_user": {
                    "email": serializer.data["email"],
                    "role": serializer.data["role"],
                },
            }
        else:
            status_code = HTTP_401_UNAUTHORIZED
            response = {
                "success": False,
                "message": "Invalid Credentials",
            }

        return Response(response, status_code)
