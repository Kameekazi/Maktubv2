from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from ..serializers import UserRegisterSerializer
from ..validations import custom_validation


class UserRegisterView(APIView):
    serializer_class = UserRegisterSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        clean_data = custom_validation(request.data)
        serializer = self.serializer_class(data=clean_data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            serializer.save()
            status_code = HTTP_201_CREATED

            response = {
                "success": True,
                "message": "User registration successful",
                "user": serializer.data,
            }
        else:
            status_code = HTTP_400_BAD_REQUEST
            response = {"success": False, "message": "User registration failed"}

        return Response(response, status=status_code)


# def post(self, request):
#     clean_data = custom_validation(request.data)
#     serializer = UserRegisterSerializer(data=clean_data)
#     if serializer.is_valid(raise_exception=True):
#         user = serializer.create(clean_data)
#         if user:
#             return Response(serializer.data, status=HTTP_201_CREATED)
#     return Response(status=HTTP_400_BAD_REQUEST)
