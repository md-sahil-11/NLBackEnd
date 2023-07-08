import uuid

from django.utils import timezone
from django.db import models

from apps.users.models import User


class CustomBaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=timezone.now)
    updated_at = models.DateTimeField(auto_now=timezone.now)

    class Meta:
        abstract = True


class Category(CustomBaseModel):
    title = models.CharField(max_length=100)


class App(CustomBaseModel):
    title = models.CharField(max_length=100, null=True, blank=True)
    link = models.CharField(max_length=150, null=True, blank=True)
    points = models.FloatField(default=0.0)
    created_by = models.ForeignKey(User, related_name="apps", on_delete=models.SET_NULL, null=True, blank=True)
    logo = models.ImageField(upload_to='images/apps', null=True, blank=True)
    category = models.ForeignKey(Category, related_name="apps", on_delete=models.SET_NULL, null=True)
    sub_category = models.ForeignKey(Category, related_name="sub_category_apps", on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ["-points", "-created_at"]


class Task(CustomBaseModel):
    app = models.OneToOneField(App, related_name="task", on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, related_name="tasks", on_delete=models.CASCADE, null=True)
    is_completed = models.BooleanField(default=False)
    screenshot = models.ImageField(upload_to='images/screenshots', null=True)

    class Meta:
        ordering = ["-updated_at", "-created_at"]
        unique_together = ["app", "user"]







