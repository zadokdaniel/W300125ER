from .models import Post, Comment
from .serializer import PostSerializer, CommentSerializer, UserSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from django.contrib.auth.models import User
from .permissions import isAdminOrModerator, IsAllowedOrOwner


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [isAdminOrModerator]


class PostViewsSet(ModelViewSet):
    name = 'PostViews'
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.DjangoModelPermissions]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentViewSet(ModelViewSet):
    name = 'CommentViews'
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAllowedOrOwner]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # def get_permissions(self):
    #     pass
