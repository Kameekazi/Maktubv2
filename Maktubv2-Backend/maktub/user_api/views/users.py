from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK, HTTP_403_FORBIDDEN
from ..serializers import UserSerializer
from ..models import AppUser


class UsersView(APIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    def get(self, request):
        user = request.user
        admin = user.role == 1

        if not admin:
            status_code = HTTP_403_FORBIDDEN
            response = {
                "success": False,
                "message": "Unauthorized access.",
            }
        else:
            users = AppUser.objects.all()  # query for all users
            serializer = self.serializer_class(users, many=True)
            status_code = HTTP_200_OK
            response = {
                "success": True,
                "message": "Successfully fetched users",
                "users": serializer.data,
            }

        return Response(response, status=status_code)
