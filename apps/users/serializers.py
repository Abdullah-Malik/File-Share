"""
Description of Serializers in the users app
"""
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    """
    Post Serializer is used in PostSearchAPIview to serialize the
    queryset in the view
    """

    class Meta:
        """
        Meta information
        """
        model = User
        fields = ['username', 'first_name', 'last_name', 'image']