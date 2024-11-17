from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=150, unique=True)
    body = models.TextField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(
        to=Category, on_delete=models.CASCADE, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_likes(self):
        return self.likes.count

    def __str__(self):
        return self.title

    
    class Meta:
        ordering = ["-created_at"]




class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        unique_together = ['user', 'post']


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()

