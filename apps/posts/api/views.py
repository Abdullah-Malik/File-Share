from rest_framework import generics
from django.http.response import JsonResponse
from django.db.models import Q

from .serializers import PostSerializer
from ..models import Post


class PostSearchAPIView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self, *args, **kwargs):
        """
        Fetch the queryset from the parent's get_queryset

        Return:
            queryset: set of objects that meet the filteration criteria
        """
        queryset = Post.objects.all()

        q = self.request.GET.get("q")
        if q:
            return queryset.filter(Q(title__icontains=q) | Q(description__icontains=q))
        return queryset

def PostSearchAPI(request):
    if request.method == 'GET':
        q = request.GET.get("q")
        posts = Post.objects.filter(Q(title__icontains=q) | Q(description__icontains=q))
        serializer = PostSerializer(posts, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False)