from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post

        fields = '__all__'                                                 # all columns
        # fields = ['id', 'title', 'content', 'created', 'updated']            # all columns
        # exclude = ['id']                                                   # all but the listed columns
