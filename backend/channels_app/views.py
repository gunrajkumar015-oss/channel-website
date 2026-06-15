from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import (
    UserProfile, Follow, Channel, Subscription,
    Video, Article, Image, Comment, Like, Notification
)
from .serializers import (
    UserProfileSerializer, FollowSerializer, ChannelSerializer,
    SubscriptionSerializer, VideoSerializer, ArticleSerializer,
    ImageSerializer, CommentSerializer, LikeSerializer, NotificationSerializer
)

class IsWriter(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.profile.user_type == 'writer'

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    @action(detail=False, methods=['get'])
    def me(self, request):
        profile = request.user.profile
        serializer = self.get_serializer(profile)
        return Response(serializer.data)

class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(follower=self.request.user)

class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    @action(detail=True, methods=['post'])
    def subscribe(self, request, pk=None):
        channel = self.get_object()
        subscription, created = Subscription.objects.get_or_create(
            user=request.user,
            channel=channel
        )
        if created:
            channel.subscribers_count += 1
            channel.save()
            return Response({'status': 'subscribed'})
        return Response({'status': 'already subscribed'})

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        channel = Channel.objects.get(owner=self.request.user)
        serializer.save(channel=channel)

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        channel = Channel.objects.get(owner=self.request.user)
        serializer.save(channel=channel)

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)
    
    @action(detail=False, methods=['post'])
    def mark_all_as_read(self, request):
        Notification.objects.filter(user=request.user, is_read=False).update(is_read=True)
        return Response({'status': 'all notifications marked as read'})
