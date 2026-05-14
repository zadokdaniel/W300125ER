from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostViews.as_view()),
    path('posts/<int:pk>/', views.PostViewByPk.as_view())
]
