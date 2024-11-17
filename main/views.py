from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from django.contrib.auth.models import User

from .models import Like, Post, Comment
from .serializers import ChangePasswordSerializer, LikeSerializer, PostCommentsSerializer, PostsSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly


class PostsAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        sorted_by = self.request.query_params.get("sorted_by", 0)
        if sorted_by == "likes":
            return Post.objects.order_by('likes')
        return Post.objects.order_by('created_at')
    serializer_class = PostsSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FavPostsAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Post.objects.filter(likes__user=self.request.user)
    serializer_class = PostsSerializer


class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]

    queryset = Post.objects.all()
    serializer_class = PostsSerializer



class PostCategoryAPIView(generics.ListAPIView):
    serializer_class = PostsSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        return Post.objects.filter(category=category)

    

class PostUserAPIView(generics.ListAPIView):
    serializer_class = PostsSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        return Post.objects.filter(user__username=username)
    


class UserUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
    

class ChangePasswordAPIView(generics.UpdateAPIView):
        serializer_class = ChangePasswordSerializer
        model = User
        permission_classes = (IsAuthenticated,)

        def get_object(self, queryset=None):
            obj = self.request.user
            return obj

        def update(self, request, *args, **kwargs):
            self.object = self.get_object()
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                if not self.object.check_password(serializer.data.get("old_password")):
                    return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                return Response(status=status.HTTP_204_NO_CONTENT)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class LikeCreateAPIView(generics.CreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        post = Post.objects.get(id=self.kwargs['pk'])
        if not Post.objects.filter(likes__user=self.request.user, id=self.kwargs['pk']):
            serializer.save(user=self.request.user, post=post)


class LikeDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_object(self):
        post = Post.objects.get(id=self.kwargs['pk'])
        return Like.objects.filter(user=self.request.user, post=post)



class PostCommentsAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post = Post.objects.get(id=self.kwargs['pk'])
        return Comment.objects.filter(post=post)
    serializer_class = PostCommentsSerializer

    def perform_create(self, serializer):
        post = Post.objects.get(id=self.kwargs['pk'])
        serializer.save(user=self.request.user, post=post)