from django.urls import include, path
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('post', views.PostViewsSet, 'post')
router.register('comment', views.CommentViewSet, 'comment')


urlpatterns = [
    path('', include(router.urls)),
]
