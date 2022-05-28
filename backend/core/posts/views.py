from .models import Post, Text
from .serializers import PostSerializer, TextSerializer
from rest_framework import viewsets


class text_detail_view(viewsets.ReadOnlyModelViewSet):
    queryset = Text.objects.all()
    serializer_class = TextSerializer

class post_details_view(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



