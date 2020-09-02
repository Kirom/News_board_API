"""Api's urls."""
from api.views import CommentViewSet, PostViewSet

from django.urls import include, path

from rest_framework import routers


router = routers.DefaultRouter()
router.register("posts", PostViewSet)
router.register("comments", CommentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
