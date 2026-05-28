from rest_framework import serializers
from .models import Post, Comment, UserProfile
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class FlatUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class FlatPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created', 'updated']


class FlatCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'created',
                  'updated', 'post_id', 'author_id']


class UserSerializer(serializers.ModelSerializer):
    posts = FlatPostSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'posts']


class CommentSerializer(serializers.ModelSerializer):
    author = FlatUserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'content', 'created', 'updated', 'author']

    def get_fields(self):
        fields = super(CommentSerializer, self).get_fields()
        request = self.context.get('request')

        if request and request.method == 'POST':
            fields['post'] = serializers.PrimaryKeyRelatedField(
                queryset=Post.objects.all())
        else:
            fields['post'] = serializers.PrimaryKeyRelatedField(read_only=True)

        return fields


class PostSerializer(serializers.ModelSerializer):
    comments = FlatCommentSerializer(many=True, read_only=True)
    owner = FlatUserSerializer(read_only=True)

    class Meta:
        model = Post

        # all columns
        fields = ['id', 'title', 'content',
                  'created', 'updated', 'comments', 'owner']
        # fields = ['id', 'title', 'content', 'created', 'updated']            # all columns
        # exclude = ['id']                                                   # all but the listed columns


class BlogTokenSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user: User):
        token = super().get_token(user)

        token['name'] = user.get_full_name()
        token['username'] = user.username
        token['claims'] = {
            'isAdmin': user.is_superuser,
            'isActive': user.is_active
        }

        return token


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = '__all__'
