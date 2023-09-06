from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class AppUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_("An email is required."))
        if not password:
            raise ValueError(_("A password is required."))
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("role", 1)

        if extra_fields.get("role") != 1:
            raise ValueError(_("Superuser must have role of Global Admin."))
        if not email:
            raise ValueError(_("An email is required."))
        if not password:
            raise ValueError(_("A password is required."))
        user = self.create_user(email, password, **extra_fields)
        user.save()
        return user
