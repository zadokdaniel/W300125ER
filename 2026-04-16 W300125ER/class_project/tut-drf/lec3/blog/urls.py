from django.urls import include, path
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('pictures', views.PicturesViewSet, 'pictures')


urlpatterns = [
    path('', include(router.urls)),
    path('posts/', views.PostViews.as_view()),
    path('posts/<int:pk>/', views.PostViewByPk.as_view())
]
