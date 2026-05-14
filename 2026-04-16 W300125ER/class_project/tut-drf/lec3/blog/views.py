from django.shortcuts import render
# from django.http import HttpRequest, JsonResponse
from .models import Post
from .serializer import PostSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request


class PostViews(APIView):
    name = 'PostViews'
    throttle_class = []
    permissions_classes = []
    authentication_classes = []

    def get(self, request: Request):
        posts = Post.objects.all()
        serialized = PostSerializer(posts, many=True)
        return Response({'posts': serialized.data})

    def post(self, request: Request):
        post = PostSerializer(data=request.data)

        if not post.is_valid:
            return Response({'errors': post.error_messages}, status=status.HTTP_400_BAD_REQUEST)

        post.save()
        return Response(post.data, status=status.HTTP_201_CREATED)


class PostViewByPk(APIView):
    name = 'PostByPkViews'
    throttle_class = []
    permissions_classes = []
    authentication_classes = []

    def get(self, request: Request, pk: int):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({'errors': 'Post not found with the id {pk}'}, status=status.HTTP_404_NOT_FOUND)
        serialized = PostSerializer(post)
        return Response({'post': serialized.data})
