from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserProfileViewSet, FollowViewSet, ChannelViewSet,
    VideoViewSet, ArticleViewSet, ImageViewSet,
    CommentViewSet, LikeViewSet, NotificationViewSet
)

router = DefaultRouter()
router.register(r'profiles', UserProfileViewSet)
router.register(r'follows', FollowViewSet)
router.register(r'channels', ChannelViewSet)
router.register(r'videos', VideoViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'images', ImageViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'likes', LikeViewSet)
router.register(r'notifications', NotificationViewSet, basename='notification')

urlpatterns = [
    path('', include(router.urls)),
]
