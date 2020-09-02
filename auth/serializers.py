"""Auth's serializers."""
from api.models import Post

from django.contrib.auth.models import Group, User

from rest_framework import serializers
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Serializes user's model."""

    # posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        """Defining metadata for group's model serializer."""

        model = User
        fields = ["id", "url", "username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True, "required": True}}

    def create(self, validated_data):
        """Create users with token."""
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """Serializes group's model."""

    class Meta:
        """Defining metadata for group's model serializer."""

        model = Group
        fields = ["url", "name"]
