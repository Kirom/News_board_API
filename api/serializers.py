"""API's serializers."""
from api.models import Comment, Post

from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    """Serializes post's model."""

    author_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        """Defining metadata for post's model serializer."""

        model = Post
        fields = [
            "id",
            "title",
            "link",
            "creation_date",
            "amount_of_upvotes",
            "author_name",
        ]

    @staticmethod
    def get_author_name(obj):
        """Represent author's name as just name instead of user's object."""
        return obj.author_name.username


class CommentSerializer(serializers.ModelSerializer):
    """Serializes comment's model."""

    author_name = serializers.SerializerMethodField()

    class Meta:
        """Defining metadata for group's model serializer."""

        model = Comment
        fields = ["id", "author_name", "content", "creation_date", "post"]

    @staticmethod
    def get_author_name(obj):
        """Represent author's name as just name instead of user's object."""
        return obj.author_name.username
