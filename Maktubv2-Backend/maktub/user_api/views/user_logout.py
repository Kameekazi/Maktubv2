from django.contrib.auth import logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


class UserLogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response(status=HTTP_200_OK)
