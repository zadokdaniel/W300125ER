from .models import Post, Comment
from .serializer import PostSerializer, CommentSerializer, UserSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from django.contrib.auth.models import User
from .permissions import isAdminOrModerator


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.DjangoModelPermissions]


class PostViewsSet(ModelViewSet):
    name = 'PostViews'
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.DjangoModelPermissions]


class CommentViewSet(ModelViewSet):
    name = 'CommentViews'
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = []

    # def get_permissions(self):
    #     pass
