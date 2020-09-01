"""API's serializers."""
from api.models import Comment, Post

from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer):
    """Serializes post's model."""

    author_name = serializers.SerializerMethodField()

    class Meta:
        """Defining metadata for group's model serializer."""

        model = Post
        fields = [
            "id",
            "url",
            "title",
            "link",
            "creation_date",
            "amount_of_upvotes",
            "author_name",
        ]

    @staticmethod
    def get_author_name(obj):
        """Represent author's name as just name instead of user's object."""
        return (
            Post.objects.select_related("author_name")
            .get(pk=obj.pk)
            .author_name.username
        )


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    """Serializes comment's model."""

    class Meta:
        """Defining metadata for group's model serializer."""

        model = Comment
        fields = [
            "id",
            "url",
            "author_name",
            "content",
            "creation_date",
            "post",
        ]
