"""Registering models in admin."""
from api.models import Comment, Post

from django.contrib import admin


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Register post model admin."""

    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Register comment model admin."""

    pass
