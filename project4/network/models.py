from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class FollowerInfluencer(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following_relations')
    influencer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='influencer_relations')
    class Meta:
        unique_together = (('follower', 'influencer'),)
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like_count = models.IntegerField(default=0)

    class Meta:
        ordering = ['-id']
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    class Meta:
        ordering = ['id']


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    class Meta:
        unique_together = (('user', 'post'),)


