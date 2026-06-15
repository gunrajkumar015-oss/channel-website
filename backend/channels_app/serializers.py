from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    UserProfile, Follow, Channel, Subscription,
    Video, Article, Image, Comment, Like, Notification
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'user_type', 'bio', 'profile_picture', 'followers_count', 'following_count', 'created_at')

class FollowSerializer(serializers.ModelSerializer):
    follower = UserSerializer(read_only=True)
    following = UserSerializer(read_only=True)
    
    class Meta:
        model = Follow
        fields = ('id', 'follower', 'following', 'created_at')

class ChannelSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    
    class Meta:
        model = Channel
        fields = ('id', 'owner', 'name', 'description', 'banner_image', 'profile_image', 'subscribers_count', 'created_at')

class SubscriptionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    channel = ChannelSerializer(read_only=True)
    
    class Meta:
        model = Subscription
        fields = ('id', 'user', 'channel', 'subscribed_at')

class VideoSerializer(serializers.ModelSerializer):
    channel = ChannelSerializer(read_only=True)
    
    class Meta:
        model = Video
        fields = ('id', 'channel', 'title', 'description', 'video_file', 'thumbnail', 'views_count', 'likes_count', 'dislikes_count', 'created_at', 'is_published')

class ArticleSerializer(serializers.ModelSerializer):
    channel = ChannelSerializer(read_only=True)
    
    class Meta:
        model = Article
        fields = ('id', 'channel', 'title', 'content', 'featured_image', 'views_count', 'likes_count', 'created_at', 'is_published')

class ImageSerializer(serializers.ModelSerializer):
    channel = ChannelSerializer(read_only=True)
    
    class Meta:
        model = Image
        fields = ('id', 'channel', 'title', 'image', 'description', 'likes_count', 'created_at')

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = ('id', 'user', 'content_type', 'video', 'article', 'image', 'text', 'likes_count', 'created_at')

class LikeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Like
        fields = ('id', 'user', 'content_type', 'video', 'article', 'image', 'comment', 'created_at')

class NotificationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    from_user = UserSerializer(read_only=True)
    
    class Meta:
        model = Notification
        fields = ('id', 'user', 'notification_type', 'from_user', 'message', 'is_read', 'created_at')
