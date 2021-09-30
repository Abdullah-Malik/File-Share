"""
Description of Serializers in the Posts app
"""
from rest_framework import serializers
from ..models import Post
from apps.users.serializers import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    """
    Post Serializer is used in PostSearchAPIview to serialize the
    queryset in the view
    """

    owner = UserSerializer(read_only=True)
    post_url = serializers.HyperlinkedIdentityField(
        view_name='post_detail',
        lookup_field='pk'
    )

    class Meta:
        """
        Meta information
        """
        model = Post
        fields = ['id','title', 'description', 'uploaded_file', 'thumbnail_image', 'date_posted','owner', 'file_type', 'post_url']