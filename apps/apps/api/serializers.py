from rest_framework import serializers

from apps.apps.models import *


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
        )