from datetime import datetime

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User, PermissionsMixin
from django.db import models

from petstagram.auth_app.managers import PetstagramUserManager


class PetstagramUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(
        default=False,
    )
    date_joined = models.DateTimeField(auto_now_add=True)
    has_profile = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = PetstagramUserManager()