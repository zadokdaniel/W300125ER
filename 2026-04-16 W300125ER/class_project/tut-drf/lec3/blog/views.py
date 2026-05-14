from django.shortcuts import render
# from django.http import HttpRequest, JsonResponse
from .models import Post
from .serializer import PostSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.mixins import *
from rest_framework.generics import GenericAPIView


class PostViews(GenericAPIView, CreateModelMixin, ListModelMixin):
    name = 'PostViews'
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request: Request):
        return self.list(request)

    def post(self, request: Request):
        return self.create(request)


class PostViewByPk(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    name = 'PostViewsByPk'
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request: Request, pk: int):
        return self.retrieve(request, pk)

    def put(self, request: Request, pk: int):
        return self.update(request, pk)

    def delete(self, request: Request, pk: int):
        return self.destroy(request, pk)
