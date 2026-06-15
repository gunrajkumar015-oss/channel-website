from django.contrib import admin
from .models import (
    UserProfile, Follow, Channel, Subscription,
    Video, Article, Image, Comment, Like, Notification
)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_type', 'followers_count', 'following_count', 'created_at')
    list_filter = ('user_type', 'created_at')
    search_fields = ('user__username', 'user__email')

@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('follower', 'following', 'created_at')
    search_fields = ('follower__username', 'following__username')

@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'subscribers_count', 'created_at')
    search_fields = ('name', 'owner__username')
    list_filter = ('created_at',)

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'channel', 'subscribed_at')
    search_fields = ('user__username', 'channel__name')

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'channel', 'views_count', 'likes_count', 'created_at')
    list_filter = ('is_published', 'created_at')
    search_fields = ('title', 'channel__name')

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'channel', 'views_count', 'likes_count', 'created_at')
    list_filter = ('is_published', 'created_at')
    search_fields = ('title', 'channel__name')

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'channel', 'likes_count', 'created_at')
    search_fields = ('title', 'channel__name')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'content_type', 'likes_count', 'created_at')
    list_filter = ('content_type', 'created_at')
    search_fields = ('user__username', 'text')

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'content_type', 'created_at')
    list_filter = ('content_type', 'created_at')
    search_fields = ('user__username',)

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'notification_type', 'is_read', 'created_at')
    list_filter = ('notification_type', 'is_read', 'created_at')
    search_fields = ('user__username', 'message')
