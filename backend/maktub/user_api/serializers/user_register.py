from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model

UserModel = get_user_model()


# register Users
class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"

    def create(self, clean_data):
        user_obj = UserModel.objects.create_user(
            email=clean_data["email"], password=clean_data["password"]
        )
        user_obj.username = clean_data["username"]
        user_obj.role = UserModel.USER
        user_obj.save()
        return user_obj
