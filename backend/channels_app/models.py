from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import FileExtensionValidator

class UserProfile(models.Model):
    USER_TYPE_CHOICES = [
        ('reader', 'Reader'),
        ('writer', 'Writer'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='reader')
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    followers_count = models.IntegerField(default=0)
    following_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.user_type}"


class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('follower', 'following')
    
    def __str__(self):
        return f"{self.follower} follows {self.following}"


class Channel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='channels')
    name = models.CharField(max_length=100)
    description = models.TextField()
    banner_image = models.ImageField(upload_to='channel_banners/', blank=True, null=True)
    profile_image = models.ImageField(upload_to='channel_profiles/', blank=True, null=True)
    subscribers_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name='channel_subscribers')
    subscribed_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'channel')
    
    def __str__(self):
        return f"{self.user} subscribed to {self.channel}"


class Video(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name='videos')
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_file = models.FileField(
        upload_to='videos/',
        validators=[FileExtensionValidator(allowed_extensions=['mp4', 'webm', 'avi', 'mov'])]
    )
    thumbnail = models.ImageField(upload_to='video_thumbnails/', blank=True, null=True)
    views_count = models.IntegerField(default=0)
    likes_count = models.IntegerField(default=0)
    dislikes_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title


class Article(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=200)
    content = models.TextField()
    featured_image = models.ImageField(upload_to='article_images/', blank=True, null=True)
    views_count = models.IntegerField(default=0)
    likes_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title


class Image(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name='gallery')
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField(blank=True, null=True)
    likes_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    CONTENT_TYPE_CHOICES = [
        ('video', 'Video'),
        ('article', 'Article'),
        ('image', 'Image'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content_type = models.CharField(max_length=20, choices=CONTENT_TYPE_CHOICES)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
    
    text = models.TextField()
    likes_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Comment by {self.user} - {self.created_at}"


class Like(models.Model):
    CONTENT_TYPE_CHOICES = [
        ('video', 'Video'),
        ('article', 'Article'),
        ('image', 'Image'),
        ('comment', 'Comment'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    content_type = models.CharField(max_length=20, choices=CONTENT_TYPE_CHOICES)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, blank=True, null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'content_type')
    
    def __str__(self):
        return f"{self.user} liked {self.content_type}"


class Notification(models.Model):
    NOTIFICATION_TYPES = [
        ('comment', 'Comment'),
        ('like', 'Like'),
        ('subscribe', 'Subscribe'),
        ('new_content', 'New Content'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES)
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_notifications', null=True, blank=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Notification for {self.user}"
