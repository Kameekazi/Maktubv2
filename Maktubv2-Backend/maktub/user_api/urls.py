from django.urls import path
from .views import (
    UserRegisterView,
    UserLoginView,
    UserLogoutView,
    UsersView,
    UserUpdateView,
)
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("token/obtain/", jwt_views.TokenObtainPairView.as_view(), name="token_create"),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path("register", UserRegisterView.as_view(), name="register"),
    path("login", UserLoginView.as_view(), name="login"),
    path("logout", UserLogoutView.as_view(), name="logout"),
    path("users", UsersView.as_view(), name="user"),
    path("user/update/<uuid:uid>", UserUpdateView.as_view(), name="user-update"),
]
