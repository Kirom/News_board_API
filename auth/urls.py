"""Auth's urls."""
from auth import views

from django.urls import include, path

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register("users", views.UserViewSet)
router.register("groups", views.GroupViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("obtain_auth_token/", obtain_auth_token),
]
