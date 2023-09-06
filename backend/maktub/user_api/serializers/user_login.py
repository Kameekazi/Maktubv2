from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.translation import gettext_lazy as _

# from django.core.exceptions import ValidationError


# Login Users
# Responsible for authenticating username and password of users
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    role = serializers.CharField(read_only=True)

    def validate(self, data):
        email = data["email"]
        password = data["password"]
        user = authenticate(email=email, password=password)

        if not user:
            raise serializers.ValidationError(_("Invalid login credentials"))

        refresh = RefreshToken.for_user(user)
        refresh_token = str(refresh)
        access_token = str(refresh.access_token)

        update_last_login(None, user)

        validation = {
            "access": access_token,
            "refresh": refresh_token,
            "email": user.email,
            "role": user.role,
        }

        return validation

    # def check_user(self, clean_data):
    #     user = authenticate(
    #         username=clean_data["email"], password=clean_data["password"]
    #     )
    #     if not user:
    #         raise ValidationError("User Not Found")
    #     return user
