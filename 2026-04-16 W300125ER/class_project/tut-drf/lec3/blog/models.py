from django.db import models
import django.core.validators as v
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    owner = models.ForeignKey(
        'auth.User', related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField(
        validators=[
            v.MinLengthValidator(5, message='Content is too short'),
        ]
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(
        'auth.User', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.post.title} - {self.content[:20]}'


class UserProfile(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE, unique=True)
    bio = models.TextField(blank=True, max_length=1000)
    profile_pic = models.ImageField(upload_to='profiles_pics', blank=True)
    birth_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def username(self):
        return self.user.username

    def __str__(self):
        return f'{self.user.username}'
