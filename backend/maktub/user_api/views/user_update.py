from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed, NotFound, bad_request
from rest_framework.status import HTTP_200_OK
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from ..serializers import UserUpdateSerializer
from ..validations import validate_uid

UserModel = get_user_model()


class UserUpdateView(UpdateAPIView):
    serializer_class = UserUpdateSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    def get_object(self, uid):
        # Check if the UID is a valid UUID
        uid = validate_uid(str(uid))
        if not uid:
            raise bad_request("Invalid UID format")

        # Retrieve the user by UID or raise a 404 response if not found
        requestUser = self.request.user
        user = get_object_or_404(UserModel, uid=uid)

        if requestUser.role != 1:
            raise AuthenticationFailed("Unauthorized access.")

        if str(user.uid) != str(uid):
            raise NotFound("User not found.")

        return user

    def update(self, request, uid):
        instance = self.get_object(uid)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=HTTP_200_OK)
