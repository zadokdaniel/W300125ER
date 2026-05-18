from rest_framework import serializers
from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post

        # all columns
        fields = ['id', 'title', 'content', 'created', 'updated', 'comments']
        # fields = ['id', 'title', 'content', 'created', 'updated']            # all columns
        # exclude = ['id']                                                   # all but the listed columns
