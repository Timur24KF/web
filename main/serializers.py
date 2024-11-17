from main.models import Like, Post, Comment
from rest_framework import serializers
from django.contrib.auth.models import User


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'body', 'category', 'total_likes']



class PostCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'body']
        



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ChangePasswordSerializer(serializers.Serializer):
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        exclude = ['user', 'post']