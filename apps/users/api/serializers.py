from django.conf import settings

from rest_framework import serializers

from django.db.models import Sum

from apps.users.models import User
from apps.applications.models import App


class UserSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    total_points = serializers.SerializerMethodField()
    task_completed = serializers.SerializerMethodField()
    task_total = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "name",
            "image",
            "created_at",
            "is_superuser",
            "points",
            "total_points",
            "task_completed",
            "task_total"
        )
        read_only_fields = (
            "created_at",
        )

    def get_total_points(self, instance):
        data = App.objects.all().aggregate(Sum("points"))
        return data["points__sum"]
    
    def get_task_completed(self, instance):
        return instance.tasks.count()
    
    def get_task_total(self, instance):
        return App.objects.count()
        