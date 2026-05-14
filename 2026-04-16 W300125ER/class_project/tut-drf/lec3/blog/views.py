from .models import Post
from .serializer import PostSerializer
from rest_framework.request import Request
from rest_framework.mixins import *
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView


class PostViews(ListCreateAPIView):
    name = 'PostViews'
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostViewByPk(RetrieveUpdateDestroyAPIView):
    name = 'PostViewsByPk'
    queryset = Post.objects.all()
    serializer_class = PostSerializer
