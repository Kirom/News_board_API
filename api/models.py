"""Api's DB models."""
from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    """Post's db model."""

    title = models.CharField(max_length=150)
    link = models.CharField(max_length=150)
    creation_date = models.DateTimeField(default=datetime.now)
    amount_of_upvotes = models.PositiveIntegerField(default=0)
    author_name = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Represent current post's as string by name field."""
        return self.title


class Comment(models.Model):
    """Comment's db model."""

    author_name = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    creation_date = models.DateTimeField(default=datetime.now)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        """Represent current comment's as string by sliced content field."""
        return self.content[0:50]
