from main.models import Like, Post, Comment
from rest_framework import serializers
from django.contrib.auth.models import User


class PostsSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'title', 'username', 'body', 'category_name', 'category', 'total_likes', 'total_comments']



class PostCommentsSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Comment
        fields = ['username', 'body']
        



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class CreateUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user

    class Meta:
        model = User
        fields = ("username", "password", )


class ChangePasswordSerializer(serializers.Serializer):
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        exclude = ['user', 'post']