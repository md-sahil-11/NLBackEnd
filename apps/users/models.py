from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

from apps.users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(default="Anonymous", max_length=100, blank=True)
    email = models.EmailField(unique=True, db_index=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    picture = models.ImageField(upload_to='images/users', null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    points = models.FloatField(default=0.0)

    USERNAME_FIELD = "email"

    objects = UserManager()