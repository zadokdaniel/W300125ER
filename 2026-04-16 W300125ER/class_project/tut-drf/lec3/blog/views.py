from .models import Post, Comment, UserProfile
from .serializer import PostSerializer, CommentSerializer, UserSerializer, UserProfileSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from django.contrib.auth.models import User
from .permissions import isAdminOrModerator, IsAllowedOrOwner
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from blog.throttling import *


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [isAdminOrModerator]


class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
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

    # throttle_mapping = {
    #     'create': (CreatePostUserThrottle, CreatePostAnonThrottle),
    #     'list': (ListPostUserThrottle, ListPostAnonThrottle),
    #     'retrieve': (RetrievePostUserThrottle, RetrievePostAnonThrottle),
    #     'update': (UpdatePostUserThrottle, UpdatePostAnonThrottle),
    #     'partial_update': (UpdatePostUserThrottle, UpdatePostAnonThrottle),
    #     'destroy': (DeletePostUserThrottle, DeletePostAnonThrottle),
    # }

    # def get_throttles(self):
    #     throttles = self.throttle_mapping.get(self.action, [])
    #     return [throttles() for throttle in throttles]

    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    throttle_rate = {
        'anon': '100/day',
        'user': '1000/day'
    }

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # def get_permissions(self):
    #     pass
