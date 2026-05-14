from .models import Post
from .serializer import PostSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action


class PicturesViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=['get'])
    def thumbnail(self, request, pk=None):
        return Response('thumbnail')


class PostViews(ListCreateAPIView):
    name = 'PostViews'
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostViewByPk(RetrieveUpdateDestroyAPIView):
    name = 'PostViewsByPk'
    queryset = Post.objects.all()
    serializer_class = PostSerializer
