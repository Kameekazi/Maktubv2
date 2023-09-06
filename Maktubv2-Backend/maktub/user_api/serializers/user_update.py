from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class UserUpdateSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = (
            "first_name",
            "last_name",
            "email",
            "username",
            "role",
        )
