from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response

from .models import Post
from .serializers import PostsSerializer
from .permissions import IsOwnerOrReadOnly


class PostsApiView(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Post.objects.all()
    serializer_class = PostsSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsOwnerOrReadOnly]

    queryset = Post.objects.all()
    serializer_class = PostsSerializer



class PostCategoryAPIView(APIView):
    def get(self, requests, pk, *args, **kwargs):
        posts = Post.objects.filter(category=pk)
        data = PostsSerializer(posts, many=True).data
        return Response(data)
    

class PostUserAPIView(APIView):
    def get(self, requests, pk, *args, **kwargs):
        posts = Post.objects.filter(user=pk)
        data = PostsSerializer(posts, many=True).data
        return Response(data)