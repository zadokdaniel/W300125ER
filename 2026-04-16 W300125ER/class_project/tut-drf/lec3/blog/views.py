from .models import Post, Comment
from .serializer import PostSerializer, CommentSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action


class PostViewsSet(ModelViewSet):
    name = 'PostViews'
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(ModelViewSet):
    name = 'CommentViews'
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
