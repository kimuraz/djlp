"""Account models serializers. """
from rest_framework import serializers

from account.models import User


class UserSerializer(serializers.ModelSerializer):
    """User serializer class."""
    class Meta:
        """Default meta class."""
        model = User
        exclude = ('password',)
