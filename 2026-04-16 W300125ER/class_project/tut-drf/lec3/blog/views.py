from django.shortcuts import render
# from django.http import HttpRequest, JsonResponse
from .models import Post
from .serializer import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request


# Create your views here.

@api_view(['GET', 'POST'])
def posts(request: Request):

    if (request.method == 'GET'):
        serialized = PostSerializer(Post.objects.all(), many=True)
        return Response({
            'posts': serialized.data
        })

    elif (request.method == 'POST'):
        post = PostSerializer(data=request.data)
        post.is_valid(raise_exception=True)
        post.save()
        return Response(post.data, status=201)


@api_view(['GET'])
def post_by_pk(request: Request, pk: int):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response({"error": "Post not found"}, status=404)

    return Response({'post': PostSerializer(post).data})
