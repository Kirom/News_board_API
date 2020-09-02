"""Api's tasks for celery"""
from News_board_API.celery import app

from api.models import Post


@app.task
def clean_upvotes():
    """Set amount_of_upvotes of every post to zero."""
    posts = Post.objects.all()
    posts.update(amount_of_upvotes=0)
