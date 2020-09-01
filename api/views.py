"""Api's views."""
from api.models import Comment, Post
from api.serializers import CommentSerializer, PostSerializer

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class PostViewSet(viewsets.ModelViewSet):
    """API endpoint that allows posts to be viewed or edited."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        """Create posts by current user authenticated via Token."""
        serializer.save(author_name=self.request.user)

    @action(methods=["POST"], detail=True)
    def upvote_post(self, request, pk=None):
        """Lets the users upvote posts."""
        post = Post.objects.get(pk=pk)
        previous_amount_of_upvotes = post.amount_of_upvotes
        post.amount_of_upvotes += 1
        post.save()
        response = {"message": "Upvoted!"}
        if post.amount_of_upvotes == previous_amount_of_upvotes:
            return Response({"message": "Something went wrong :("})
        return Response(response)


class CommentViewSet(viewsets.ModelViewSet):
    """API endpoint that allows posts to be viewed or edited."""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        """Create comments by current user authenticated via Token."""
        serializer.save(author_name=self.request.user)
