from django.urls import path, include
from .views import *


urlpatterns = [
    path("posts/user/<int:pk>", PostUserAPIView.as_view()),
    path("posts/category/<int:pk>", PostCategoryAPIView.as_view()),
    path("posts", PostsApiView.as_view()), 
    path("post/<int:pk>", PostDetailApiView.as_view()), 

    path("auth", include("rest_framework.urls")),
]
