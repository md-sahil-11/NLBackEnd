from django.conf import settings

from rest_framework import serializers

from apps.users.models import User
from apps.users.selectors import add_token_to_user_serializer_selector


class UserSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "name",
            "image",
            "created_at",
            "is_superuser"
        )
        read_only_fields = (
            "created_at",
        )
    
    def to_representation(self, instance):
        data = super(UserSerializer, self).to_representation(instance)
        data = add_token_to_user_serializer_selector(data, instance)
        return data
    
    # def get_picture(self, instance):
    #     return instance.picture.url if instance.picture else None