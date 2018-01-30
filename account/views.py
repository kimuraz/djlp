"""Viewsets for account app."""
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from account.models import User
from account.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """User viewset."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permissions = (IsAdminUser,)


class ProfileViewSet(viewsets.ModelViewSet):
    """User profile viewset."""
    serializer_class = UserSerializer
    permissions = (IsAuthenticated,)

    def get_object(self):
        return self.request.user
