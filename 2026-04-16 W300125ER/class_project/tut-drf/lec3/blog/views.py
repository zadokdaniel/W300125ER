from .models import Post
from .serializer import PostSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action


class PicturesViewSet(ViewSet):

    def list(self, request):
        return Response('list')

    def create(self, request):
        return Response('create')

    def retrieve(self, request, pk=None):
        return Response('retrieve')

    def update(self, request, pk=None):
        return Response('update')

    def partial_update(self, request, pk=None):
        return Response('partial_update')

    def destroy(self, request, pk=None):
        return Response('destroy')

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
