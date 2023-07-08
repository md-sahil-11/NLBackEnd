from rest_framework import serializers

from apps.apps.models import *
from apps.users.api.serializers import UserSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class AppSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(
        source="category",
        queryset=Category.objects.all(), 
        write_only=True, 
        required=True
    )
    category = CategorySerializer(read_only=True)
    sub_category_id = serializers.PrimaryKeyRelatedField(
        source="sub_category",
        queryset=Category.objects.all(), 
        write_only=True, 
        required=True
    )
    sub_category = CategorySerializer(read_only=True)
    logo = serializers.ImageField(required=False)
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    task_id = serializers.CharField(source="task.id", read_only=True)
    task_screenshot = serializers.ImageField(source="task.screenshot", read_only=True)

    class Meta:
        model = App
        fields = (
            "id",
            "title",
            "link",
            "points",
            "created_by",
            "logo",
            "category_id",
            "category",
            "sub_category_id",
            "sub_category",
            "task_id",
            "task_screenshot"
        )


class TaskSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(
        source="user",
        queryset=User.objects.all(), 
        write_only=True, 
        required=True
    )
    user = UserSerializer(read_only=True)
    app_id = serializers.PrimaryKeyRelatedField(
        source="app",
        queryset=App.objects.all(), 
        write_only=True, 
        required=True
    )
    app = AppSerializer(read_only=True)
    screenshot = serializers.ImageField(required=False)
    
    class Meta:
        model = Task
        fields = (
            "id",
            "app",
            "app_id",
            "user",
            "user_id",
            "is_completed",
            "screenshot",
        )